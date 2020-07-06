from .abstract_parser import AbstractParser


class CSVParser(AbstractParser):
    def __init__(self, source):
        super(CSVParser, self).__init__(source)

    def _parse(self, source) -> list:
        lines = source.decode('ascii').split('\n')
        res = list(map(lambda item: item.split(','), lines))
        return res

    def is_loaded(self):
        return len(self._source) > 0
