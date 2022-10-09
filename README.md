# jupyter-notebook-parser
A Python library to parse cell contents from Jupyter notebooks


## Installation

```bash
pip install jupyter-notebook-parser
```

## Usage

### Parser

```python
from jupyter_notebook_parser import JupyterNotebookParser


parsed = JupyterNotebookParser('my_notebook.ipynb')

parsed.get_all_cells()  # returns List[Dict], each Dict is a notebook cell

parsed.get_markdown_cells()  # returns List[Dict], each Dict is a markdown cel
parsed.get_markdown_cell_indices()  # returns List[int], each is a markdown cell's index
parsed.get_markdown_cell_sources()  # returns List[str], each is a markdown cell's text

parsed.get_code_cells()  # returns List[Dict], each Dict is a code cell
parsed.get_code_cell_indices()  # returns List[int], each int is a code cell's index
parsed.get_code_cell_sources()  # returns List[SourceCodeContainer]

source = parsed.get_code_cell_sources()[0]
source.raw_source  # str
source.source_without_magic  # str (all ipython magics excluded)
source.magics  # Dict[int, str] (all magics, from line number to magic text)
```

### Rewriter

```python
from jupyter_notebook_parser import JupyterNotebookParser
from jupyter_notebook_parser import JupyterNotebookRewriter


parsed = JupyterNotebookParser('my_notebook.ipynb')
rewriter = JupyterNotebookRewriter(parsed_notebook=parsed)

rewriter.replace_source_in_code_cell(index=5, new_source='print(2)')
```

### Source code container
```python
from jupyter_notebook_parser import SourceCodeContainer


container = SourceCodeContainer('a = 2\n%timeit b = 2 ** 10\nprint(b)')
container.raw_source  # same as the input
container.source_without_magic  # 'a = 2\n b = 2 ** 10\nprint(b)'
container.magics  # {1: '%timeit'}
```
