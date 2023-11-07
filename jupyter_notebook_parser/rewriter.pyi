import sys

if sys.version_info < (3, 10):
    from typing import List
else:
    List = list

from jupyter_notebook_parser.parser import JupyterNotebookParser


class JupyterNotebookRewriter:
    notebook: JupyterNotebookParser

    def __init__(self, parsed_notebook: JupyterNotebookParser) -> None: ...

    def replace_source_in_code_cell(self, index: int, new_source: str) -> None: ...

    @staticmethod
    def split_into_lines(text_content: str) -> List[str]: ...
