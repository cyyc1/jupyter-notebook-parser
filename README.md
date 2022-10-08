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

all_cells = parser.get_all_cells()  # List[Dict], each Dict is a notebook cell

code_cells = parser.get_code_cells()  # List[Dict], each Dict is a code cell
code_cell_indices = parser.get_code_cell_indices()  # List[int], each int is the index of the code cell
code_cell_sources = parser.get_code_cell_sources()  # List[str], each str is the source code of the code cell

markdown_cells = parser.get_markdown_cells()  # List[Dict], each Dict is a markdown cel
markdown_cell_indices = parser.get_markdown_cell_indices()  # List[int]
markdown_sources = parser.get_markdown_cell_sources()  # List[str], each str is the raw markdown text
```
