from lxml.html import fromstring
from ..items.generator_constants import GeneratorConstants as data_types
from ..parsers.csv_parser import CSVParser
from ..parsers.html_parser import HTMLParser
from ..parsers.abstract_parser import AbstractParser


class Response:
    DATA_HTML_TYPE = 'html'
    DATA_UNKNOWN_TYPE = 'unknown'

    def __init__(self, source, header: str):
        self.content_type = self._get_content_type(header)
        self.content = self._parse(source)

    def _parse(self, source) -> AbstractParser or None:
        if self.content_type == self.DATA_HTML_TYPE:
            return HTMLParser(source)
        elif self.content_type == data_types.DATA_TYPE_CSV:
            return CSVParser(source)
        else:
            return None

    def _get_content_type(self, header: str) -> str:
        if header.find('text/html') >= 0:
            return self.DATA_HTML_TYPE
        if header.find('text/csv') >= 0:
            return data_types.DATA_TYPE_CSV
        # Another types should be added here
        else:
            return self.DATA_UNKNOWN_TYPE
