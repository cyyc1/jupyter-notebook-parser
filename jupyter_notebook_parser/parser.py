import json
from os.path import splitext

from jupyter_notebook_parser.container import SourceCodeContainer


class JupyterNotebookParser:
    __notebook_corrupted_msg = "This notebook file is possibly corrupted"

    __slots__ = ("notebook_content",)

    @classmethod
    def open_from_file(cls, filename, *, assert_file_ext=True, encoding=None):
        if assert_file_ext:
            _, ext = splitext(filename)
            if ext != ".ipynb":
                raise NameError("This file is not a Jupyter notebook")

            with open(filename, "rt", encoding=encoding) as fp:
                return cls.read_from_stream(fp)

    @classmethod
    def read_from_stream(cls, fp):
        try:
            content = json.load(fp)
        except json.JSONDecodeError as jde:
            raise ValueError(cls.__notebook_corrupted_msg) from jde
        return cls(content)

    @classmethod
    def read_from_string(cls, source):
        try:
            content = json.loads(source)
        except json.JSONDecodeError as jde:
            raise ValueError(cls.__notebook_corrupted_msg) from jde
        return cls(content)

    def __init__(self, notebook_content):
        self.notebook_content = notebook_content

    def get_all_cells(self):
        if "cells" not in self.notebook_content:
            raise ValueError(self.__notebook_corrupted_msg)

        return self.notebook_content["cells"]

    def get_code_cell_indices(self):
        return self._get_cell_indices(type_="code")

    def get_code_cells(self):
        return self.__get_cells(type_="code")

    def get_code_cell_sources(self):
        code_cells = self.get_code_cells()
        raw_sources = self.__join_lines_in_cells(cells=code_cells)
        return [SourceCodeContainer(_) for _ in raw_sources]

    def get_markdown_cell_indices(self):
        return self._get_cell_indices(type_="markdown")

    def get_markdown_cells(self):
        return self.__get_cells(type_="markdown")

    def get_markdown_cell_sources(self):
        markdown_cells = self.get_markdown_cells()
        return self.__join_lines_in_cells(cells=markdown_cells)

    def _get_cell_indices(self, type_):
        self.__validate_type_arg(type_)
        indices_of_code_cells = []
        for i, cell in enumerate(self.get_all_cells()):
            if cell.get("cell_type") == type_:
                indices_of_code_cells.append(i)

        return indices_of_code_cells

    def __get_cells(self, type_):
        self.__validate_type_arg(type_)
        all_cells = self.get_all_cells()
        return [cell for cell in all_cells if cell["cell_type"] == type_]

    def __join_lines_in_cells(self, cells):
        all_cell_sources = []
        for cell in cells:
            self.__check_source_in_cell(cell)
            joined_lines = self.__join_source_lines(cell.get("source", ""))
            all_cell_sources.append(joined_lines)

        return all_cell_sources

    @staticmethod
    def __join_source_lines(lines, append_newline=False):
        joined = ''.join(lines)
        return joined + '\n' if append_newline else joined

    @staticmethod
    def __validate_type_arg(type_):
        if type_ not in {"code", "markdown"}:
            raise ValueError("Invalid `type` value")

    def __check_source_in_cell(self, cell):
        if 'source' not in cell:
            raise ValueError(self.__notebook_corrupted_msg)
