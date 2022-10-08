import json
from typing import List, Dict


class JupyterNotebookParser:
    def __init__(self, notebook_filename: str) -> None:
        if not notebook_filename.endswith('.ipynb'):
            raise NameError('This file is not a Jupyter notebook')

        try:
            with open(notebook_filename) as fp:
                notebook_content = json.load(fp)
        except json.JSONDecodeError:
            raise IOError('Error loading this notebook. File corrupted?')
        else:
            self.notebook_content: Dict = notebook_content

    def get_code_cells(self) -> List[str]:
        return self._get_cells(type_='code')

    def get_markdown_cells(self) -> List[str]:
        return self._get_cells(type_='markdown')

    def _get_cells(self, type_: str) -> List[str]:
        if 'cells' not in self.notebook_content:
            raise IOError('This notebook file is possibly corrupted.')

        if type_ not in {'code', 'markdown'}:
            raise ValueError('Invalid `type` value')

        qualifying_cells = [
            cell['source']
            for cell in self.notebook_content['cells']
            if cell['cell_type'] == type_
        ]
        return [''.join(_) for _ in qualifying_cells]
