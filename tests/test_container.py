import pytest

from jupyter_notebook_parser.container import SourceCodeContainer
from jupyter_notebook_parser.container import reconstruct_source


test_cases = [
    (
        'a = 2\nprint(a)',
        ['a = 2', 'print(a)'],
        {},
    ),
    (
        'a = 2\n%timeit 2 ** 10\n\n%something',
        ['a = 2', ' 2 ** 10', '', ''],
        {1: '%timeit', 3: '%something'},
    ),
    (
        '%%time\na = 2\nprint(a)',
        ['', 'a = 2', 'print(a)'],
        {0: '%%time'},
    ),
    (
        '%%bash\ncd .',
        ['', 'cd .'],
        {0: '%%bash'},
    ),
    (
        '%%latex print(2)\n\\[ \\sin(x) \\]',
        [' print(2)', '\\[ \\sin(x) \\]'],
        {0: '%%latex'},
    ),
]


@pytest.mark.parametrize('source, expected_lines, expected_magics', test_cases)
def test_parse_source(source, expected_lines, expected_magics):
    lines_new, magics = SourceCodeContainer.parse_source(source)
    assert lines_new == expected_lines
    assert magics == expected_magics


@pytest.mark.parametrize('source', [_[0] for _ in test_cases])
def test_reconstruct_source(source):
    container = SourceCodeContainer(source)
    source_code_to_reconstruct = '\n'.join(container.lines_without_magic)
    source_new = reconstruct_source(source_code_to_reconstruct, container.magics)
    assert source_new == source
