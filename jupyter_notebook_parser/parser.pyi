import sys
from _typeshed import SupportsRead
from typing import Union

if sys.version_info < (3, 10):
    from typing import List, Dict
else:
    List = list
    Dict = dict

from jupyter_notebook_parser.container import SourceCodeContainer


class JupyterNotebookParser:
    notebook_content: Dict

    @classmethod
    def open_from_file(
            cls,
            filename: str,
            *,
            assert_file_ext: bool = True,
            encoding: Union[str, None] = None
    ) -> JupyterNotebookParser: ...

    @classmethod
    def read_from_stream(cls, fp: SupportsRead[str | bytes]) -> JupyterNotebookParser: ...

    @classmethod
    def read_from_string(cls, source: str) -> JupyterNotebookParser: ...

    def __init__(self, notebook_content: Dict) -> None: ...

    def get_all_cells(self) -> List[Dict]: ...

    def get_code_cell_indices(self) -> List[int]: ...

    def get_code_cells(self) -> List[Dict]: ...

    def get_code_cell_sources(self) -> List[SourceCodeContainer]: ...

    def get_markdown_cell_indices(self) -> List[int]: ...

    def get_markdown_cells(self) -> List[Dict]: ...

    def get_markdown_cell_sources(self) -> List[str]: ...

    def _get_cell_indices(self, type_: str) -> List[int]: ...
