import re


class SourceCodeContainer:
    __ipython_line_magic = re.compile(r"^(%\S+)($|\s.*)")  # https://regex101.com/r/LTQpNc/1
    __ipython_cell_magic = re.compile(r"^(%%\S+)($|\s.*)")

    __slots__ = ("raw_source", "lines_without_magic", "magics", "source_without_magic")

    def __init__(self, raw_source):
        self.raw_source = raw_source

        lines_without_magic, magics = self.parse_source(raw_source)
        self.lines_without_magic = lines_without_magic
        self.magics = magics

        self.source_without_magic = '\n'.join(self.lines_without_magic)

    @classmethod
    def parse_source(cls, raw_source):
        lines = raw_source.split('\n')
        lines_new = []
        magics = {}
        for i, line in enumerate(lines):
            m = cls.__ipython_cell_magic.match(line)
            if m is not None:  # ipython cell magic
                magics[i] = m.group(1)
                lines_new.append(m.group(2))
                continue

            m = cls.__ipython_line_magic.match(line)
            if m is not None:  # ipython line magic
                magics[i] = m.group(1)
                lines_new.append(m.group(2))
                continue

            # does not contain any ipython magic
            lines_new.append(line)

        return lines_new, magics


def reconstruct_source(source_code, magics):
    lines = source_code.split('\n')
    lines_new = [magics.get(i, "") + line for i, line in enumerate(lines)]
    return '\n'.join(lines_new)
