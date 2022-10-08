import os

from jupyter_notebook_parser import JupyterNotebookParser

THIS_FILE_DIR = os.path.abspath(os.path.dirname(__file__))
RESOURCE_DIR = os.path.join(THIS_FILE_DIR, 'resources')


def test_parser_get_code_cells():
    filename = os.path.join(RESOURCE_DIR, 'jupyter_notebook_1.ipynb')
    parser = JupyterNotebookParser(filename)
    code_cells = parser.get_code_cells()
    expected_cells = [
        'from typing import List, Dict',
        'def some_function(arg1: List[str], arg2: Dict[str, float]):\n    print(arg1)\n    return arg2',  # noqa: E501
        "a = some_function(['a', 'b'], {'c': 0.2})",
        'assert 3 == 3',
        'def some_other_function() -> bool:\n    """\n    Some docstring\n    """\n    return False',  # noqa: E501
        'print(some_other_function())',
        'print(\'abcd"efg".\')',
    ]
    assert code_cells == expected_cells


def test_parser_get_markdown_cells():
    filename = os.path.join(RESOURCE_DIR, 'jupyter_notebook_1.ipynb')
    parser = JupyterNotebookParser(filename)
    code_cells = parser.get_markdown_cells()
    expected_cells = [
        '## Section 1',
        'Here is a math formula:\n\n$$c = \sqrt{a^2 + b^2}$$',  # noqa: W605
        'Some texts.',
        '### Some more texts\n\n| Syntax      | Description |\n| ----------- | ----------- |\n| Header      | Title       |\n| Paragraph   | Text        |',  # noqa: E501
    ]
    assert code_cells == expected_cells
