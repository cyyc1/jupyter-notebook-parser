import sys

if sys.version_info < (3, 10):
    from typing import Tuple, List, Dict
else:
    List = list
    Tuple = tuple
    Dict = dict


class SourceCodeContainer:
    raw_source: str
    lines_without_magic: List[str]
    magics: Dict[int, str]
    source_without_magic: str

    def __init__(self, raw_source: str) -> None: ...

    @classmethod
    def parse_source(cls, raw_source: str) -> Tuple[List[str], Dict[int, str]]: ...


def reconstruct_source(source_code: str, magics: Dict[int, str]) -> str: ...
