import json
from typing import List, Dict

from jupyter_notebook_parser.container import SourceCodeContainer


class JupyterNotebookParser:
    def __init__(self, notebook_filename: str) -> None:
        if not notebook_filename.endswith('.ipynb'):
            raise NameError('This file is not a Jupyter notebook')

        self.notebook_corrupted_msg = 'This notebook file is possibly corrupted'
        try:
            with open(notebook_filename) as fp:
                notebook_content = json.load(fp)
        except json.JSONDecodeError:
            raise ValueError(self.notebook_corrupted_msg)
        else:
            self.notebook_content: Dict = notebook_content

    def get_all_cells(self) -> List[Dict]:
        if 'cells' not in self.notebook_content:
            raise ValueError(self.notebook_corrupted_msg)

        return self.notebook_content['cells']

    def get_code_cell_indices(self) -> List[int]:
        return self._get_cell_indices(type_='code')

    def get_code_cells(self) -> List[Dict]:
        return self._get_cells(type_='code')

    def get_code_cell_sources(self) -> List[SourceCodeContainer]:
        code_cells = self.get_code_cells()
        raw_sources: List[str] = self._join_lines_in_cells(cells=code_cells)
        return [SourceCodeContainer(_) for _ in raw_sources]

    def get_markdown_cell_indices(self) -> List[int]:
        return self._get_cell_indices(type_='markdown')

    def get_markdown_cells(self) -> List[Dict]:
        return self._get_cells(type_='markdown')

    def get_markdown_cell_sources(self) -> List[str]:
        markdown_cells = self.get_markdown_cells()
        return self._join_lines_in_cells(cells=markdown_cells)

    def _get_cell_indices(self, type_: str) -> List[int]:
        self._validate_type_arg(type_)
        indices_of_code_cells = []
        for i, cell in enumerate(self.get_all_cells()):
            if cell.get('cell_type') == type_:
                indices_of_code_cells.append(i)

        return indices_of_code_cells

    def _get_cells(self, type_: str) -> List[Dict]:
        self._validate_type_arg(type_)
        all_cells = self.get_all_cells()
        return [cell for cell in all_cells if cell['cell_type'] == type_]

    def _join_lines_in_cells(self, cells: List[Dict]) -> List[str]:
        all_cell_sources = []
        for cell in cells:
            self._check_source_in_cell(cell)
            joined_lines = self._join_source_lines(cell.get('source', ''))
            all_cell_sources.append(joined_lines)

        return all_cell_sources

    @classmethod
    def _join_source_lines(
            cls,
            lines: List[str],
            append_newline: bool = False,
    ) -> str:
        joined = ''.join(lines)
        return joined + '\n' if append_newline else joined

    @classmethod
    def _validate_type_arg(cls, type_: str) -> None:
        if type_ not in {'code', 'markdown'}:
            raise ValueError('Invalid `type` value')

    def _check_source_in_cell(self, cell: Dict) -> None:
        if 'source' not in cell:
            raise ValueError(self.notebook_corrupted_msg)
