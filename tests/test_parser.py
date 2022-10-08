import os
import pytest

from jupyter_notebook_parser import JupyterNotebookParser

THIS_FILE_DIR = os.path.abspath(os.path.dirname(__file__))
RESOURCE_DIR = os.path.join(THIS_FILE_DIR, 'resources')


expected_all_cells = [
    {
        'cell_type': 'code',
        'execution_count': 1,
        'id': '1a4e6df0',
        'metadata': {},
        'outputs': [],
        'source': [
            'from typing import List, Dict'
        ]
    },
    {
        'cell_type': 'code',
        'execution_count': 2,
        'id': 'd72a909f',
        'metadata': {},
        'outputs': [],
        'source': [
            'def some_function(arg1: List[str], arg2: Dict[str, float]):\n',
            '    print(arg1)\n',
            '    return arg2'
        ]
    },
    {
        'cell_type': 'markdown',
        'id': '0040a4f4',
        'metadata': {},
        'source': [
            '## Section 1'
        ]
    },
    {
        'cell_type': 'code',
        'execution_count': 3,
        'id': '3a1b985c',
        'metadata': {},
        'outputs': [
            {
                'name': 'stdout',
                'output_type': 'stream',
                'text': [
                    "['a', 'b']\n"
                ]
            }
        ],
        'source': [
            "a = some_function(['a', 'b'], {'c': 0.2})"
        ]
    },
    {
        'cell_type': 'code',
        'execution_count': 4,
        'id': '2dfd7d0b',
        'metadata': {},
        'outputs': [],
        'source': [
            'assert 3 == 3'
        ]
    },
    {
        'cell_type': 'markdown',
        'id': 'de5a89c9',
        'metadata': {},
        'source': [
            'Here is a math formula:\n',
            '\n',
            '$$c = \\sqrt{a^2 + b^2}$$'
        ]
    },
    {
        'cell_type': 'code',
        'execution_count': 5,
        'id': '4952b6de',
        'metadata': {},
        'outputs': [],
        'source': [
            'def some_other_function() -> bool:\n',
            '    """\n',
            '    Some docstring\n',
            '    """\n',
            '    return False'
        ]
    },
    {
        'cell_type': 'markdown',
        'id': 'bf1cb851',
        'metadata': {},
        'source': [
            'Some texts.'
        ]
    },
    {
        'cell_type': 'code',
        'execution_count': 6,
        'id': '01224536',
        'metadata': {},
        'outputs': [
            {
             'name': 'stdout',
             'output_type': 'stream',
             'text': [
              'False\n'
             ]
            }
        ],
        'source': [
            'print(some_other_function())'
        ]
    },
    {
        'cell_type': 'markdown',
        'id': 'b54d0660',
        'metadata': {},
        'source': [
            '### Some more texts\n',
            '\n',
            '| Syntax      | Description |\n',
            '| ----------- | ----------- |\n',
            '| Header      | Title       |\n',
            '| Paragraph   | Text        |'
        ]
    },
    {
        'cell_type': 'code',
        'execution_count': 7,
        'id': 'dc0edb11',
        'metadata': {},
        'outputs': [
            {
                 'name': 'stdout',
                 'output_type': 'stream',
                 'text': [
                     'abcd"efg".\n'
                 ]
            }
        ],
        'source': [
            "print('abcd\"efg\".')"
        ]
    }
]


def test_parser_get_all_cells():
    filename = os.path.join(RESOURCE_DIR, 'jupyter_notebook_1.ipynb')
    parser = JupyterNotebookParser(filename)
    all_cells = parser.get_all_cells()
    assert all_cells == expected_all_cells


def test_parser_get_code_cells():
    filename = os.path.join(RESOURCE_DIR, 'jupyter_notebook_1.ipynb')
    parser = JupyterNotebookParser(filename)
    code_cells = parser.get_code_cells()
    expected_code_cells = [
        expected_all_cells[0],
        expected_all_cells[1],
        expected_all_cells[3],
        expected_all_cells[4],
        expected_all_cells[6],
        expected_all_cells[8],
        expected_all_cells[10],
    ]
    assert code_cells == expected_code_cells

def test_parser_get_code_cell_indices():
    filename = os.path.join(RESOURCE_DIR, 'jupyter_notebook_1.ipynb')
    parser = JupyterNotebookParser(filename)
    code_cell_indices = parser.get_code_cell_indices()
    expected_indices = [0, 1, 3, 4, 6, 8, 10]
    assert code_cell_indices == expected_indices

def test_parser_get_code_cell_sources():
    filename = os.path.join(RESOURCE_DIR, 'jupyter_notebook_1.ipynb')
    parser = JupyterNotebookParser(filename)
    code_sources = parser.get_code_cell_sources()
    expected_sources = [
        'from typing import List, Dict',
        'def some_function(arg1: List[str], arg2: Dict[str, float]):\n    print(arg1)\n    return arg2',  # noqa: E501
        "a = some_function(['a', 'b'], {'c': 0.2})",
        'assert 3 == 3',
        'def some_other_function() -> bool:\n    """\n    Some docstring\n    """\n    return False',  # noqa: E501
        'print(some_other_function())',
        'print(\'abcd"efg".\')',
    ]
    assert code_sources == expected_sources

def test_parser_get_markdown_cells():
    filename = os.path.join(RESOURCE_DIR, 'jupyter_notebook_1.ipynb')
    parser = JupyterNotebookParser(filename)
    markdown_cells = parser.get_markdown_cells()
    expected_markdown_cells = [
        expected_all_cells[2],
        expected_all_cells[5],
        expected_all_cells[7],
        expected_all_cells[9],
    ]
    assert markdown_cells == expected_markdown_cells

def test_parser_get_markdown_cell_indices():
    filename = os.path.join(RESOURCE_DIR, 'jupyter_notebook_1.ipynb')
    parser = JupyterNotebookParser(filename)
    markdown_cell_indices = parser.get_markdown_cell_indices()
    expected_indices = [2, 5, 7, 9]
    assert markdown_cell_indices == expected_indices

def test_parser_get_markdown_cell_sources():
    filename = os.path.join(RESOURCE_DIR, 'jupyter_notebook_1.ipynb')
    parser = JupyterNotebookParser(filename)
    markdown_sources = parser.get_markdown_cell_sources()
    expected_sources = [
        '## Section 1',
        'Here is a math formula:\n\n$$c = \sqrt{a^2 + b^2}$$',  # noqa: W605
        'Some texts.',
        '### Some more texts\n\n| Syntax      | Description |\n| ----------- | ----------- |\n| Header      | Title       |\n| Paragraph   | Text        |',  # noqa: E501
    ]
    assert markdown_sources == expected_sources

def test_not_ipynb_file():
    with pytest.raises(NameError):
        JupyterNotebookParser(os.path.join(RESOURCE_DIR, 'test.txt'))


def test_corrupted_ipynb_file_1():
    with pytest.raises(ValueError):
        filename = os.path.join(RESOURCE_DIR, 'invalid_notebook_1.ipynb')
        parser = JupyterNotebookParser(filename)
        parser.get_markdown_cell_sources()


def test_corrupted_ipynb_file_2():
    with pytest.raises(ValueError):
        filename = os.path.join(RESOURCE_DIR, 'invalid_notebook_2.ipynb')
        JupyterNotebookParser(filename)
