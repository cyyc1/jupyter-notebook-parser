# jupyter-notebook-parser
A Python library to parse cell contents from Jupyter notebooks


## Installation

```bash
pip install jupyter-notebook-parser
```

## Usage

```python
from jupyter_notebook_parser import JupyterNotebookParser

parser = JupyterNotebookParser('my_notebook.ipynb')

parser.get_all_cells()  # returns List[Dict], each Dict is a notebook cell

parser.get_code_cells()  # returns List[Dict], each Dict is a code cell
parser.get_code_cell_indices()  # returns List[int], each int is a code cell's index
parser.get_code_cell_sources()  # returns List[str], each str is a code cell's Python code

parser.get_markdown_cells()  # returns List[Dict], each Dict is a markdown cel
parser.get_markdown_cell_indices()  # returns List[int], each is a markdown cell's index
parser.get_markdown_cell_sources()  # returns List[str], each is a markdown cell's text
```
