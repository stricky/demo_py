from .abstract_parser import AbstractParser
from lxml.html import fromstring


class HTMLParser(AbstractParser):
    def __init__(self, source):
        super(HTMLParser, self).__init__(source)
        self._xpaths = {
            'error': '//*[contains(@class,"alert-danger")]'
        }

    def _parse(self, source: str):
        return fromstring(source)

    def is_loaded(self) -> bool:
        response = self._source.xpath(self._xpaths['error'])
        if response[0].text_content() is None:
            return False
        return True
