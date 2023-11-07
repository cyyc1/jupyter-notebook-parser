
from jupyter_notebook_parser.parser import JupyterNotebookParser


def _split_lines(source: str):
    out = []
    end = 0
    while True:
        start = end
        end = source.find('\n', start)
        if end < 0:
            out.append(source[start:])
            return out
        out.append(source[start:end + 1])


class JupyterNotebookRewriter:
    __slots__ = ("notebook",)

    def __init__(self, parsed_notebook):
        self.notebook = parsed_notebook

    def replace_source_in_code_cell(self, index, new_source) -> None:
        self.notebook.notebook_content["cells"][index]["source"] = _split_lines(new_source)

    @staticmethod
    def split_into_lines(text_content):
        lines_temp = text_content.split('\n')
        return [_ + '\n' for _ in lines_temp[:-1]] + [lines_temp[-1]]
