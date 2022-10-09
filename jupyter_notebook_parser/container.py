import re
from typing import Tuple, List, Dict

ipython_line_magic = re.compile(r'^(%\S+)($|\s.*)')  # https://regex101.com/r/LTQpNc/1
ipython_cell_magic = re.compile(r'^(%%\S+)($|\s.*)')


class SourceCodeContainer:
    def __init__(self, raw_source: str) -> None:
        self.raw_source = raw_source

        lines_without_magic, magics = self.parse_source(raw_source)
        self.lines_without_magic = lines_without_magic
        self.magics = magics

        self.source_without_magic = '\n'.join(self.lines_without_magic)

    @classmethod
    def parse_source(cls, raw_source: str) -> Tuple[List[str], Dict[int, str]]:
        lines = raw_source.split('\n')
        lines_new = []
        magics = {}
        for i, line in enumerate(lines):
            if line.startswith('%%'):  # ipython cell magic
                match_obj = ipython_cell_magic.match(line)
                magics[i] = match_obj.group(1)
                lines_new.append(match_obj.group(2))
            elif line.startswith('%'):  # ipython line magic
                match_obj = ipython_line_magic.match(line)
                magics[i] = match_obj.group(1)
                lines_new.append(match_obj.group(2))
            else:  # does not contain any ipython magic
                lines_new.append(line)

        return lines_new, magics


def reconstruct_source(source_code: str, magics: Dict[int, str]) -> str:
    lines = source_code.split('\n')
    lines_new = [magics.get(i, '') + line for i, line in enumerate(lines)]
    return '\n'.join(lines_new)
