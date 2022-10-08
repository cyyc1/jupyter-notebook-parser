import os
import pytest

from jupyter_notebook_parser import JupyterNotebookParser
from jupyter_notebook_parser import JupyterNotebookRewriter


THIS_FILE_DIR = os.path.abspath(os.path.dirname(__file__))
RESOURCE_DIR = os.path.join(THIS_FILE_DIR, 'resources')


def test_replace_source_in_code_cell():
    filename_before = os.path.join(RESOURCE_DIR, 'test_replace_before.ipynb')
    filename_after = os.path.join(RESOURCE_DIR, 'test_replace_after.ipynb')
    parsed_before = JupyterNotebookParser(filename_before)
    parsed_after = JupyterNotebookParser(filename_after)

    assert parsed_before.notebook_content != parsed_after.notebook_content

    rewriter = JupyterNotebookRewriter(parsed_before)
    rewriter.replace_source_in_code_cell(
        index=1,
        new_source='def square_root(a: int):\n    return a ** 0.5',
    )
    rewriter.replace_source_in_code_cell(
        index=4,
        new_source='print(math.gcd(12, 16))',
    )
    assert parsed_before.notebook_content == parsed_after.notebook_content


def test_replace_source_in_code_cell__index_out_of_range():
    filename = os.path.join(RESOURCE_DIR, 'test_replace_before.ipynb')
    parsed = JupyterNotebookParser(filename)
    rewriter = JupyterNotebookRewriter(parsed)
    with pytest.raises(IndexError):
        rewriter.replace_source_in_code_cell(index=1000, new_source='')
