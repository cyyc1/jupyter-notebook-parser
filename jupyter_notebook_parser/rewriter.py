from typing import List

from jupyter_notebook_parser.parser import JupyterNotebookParser


class JupyterNotebookRewriter:
    def __init__(self, parsed_notebook: JupyterNotebookParser):
        self.notebook = parsed_notebook

    def replace_source_in_code_cell(self, index: int, new_source: str) -> None:
        new_lines = self.split_into_lines(text_content=new_source)
        self.notebook.notebook_content['cells'][index]['source'] = new_lines

    @classmethod
    def split_into_lines(cls, text_content: str) -> List[str]:
        lines_temp = text_content.split('\n')
        return [_ + '\n' for _ in lines_temp[:-1]] + [lines_temp[-1]]
