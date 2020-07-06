import requests
from lxml.html import fromstring, HTMLParser
import pytest


class Session:
    def __init__(self, url):
        self.url = url
        self.csrf = self._get_csrf()

    def _get_csrf(self) -> str:
        result = requests.get(self.url)
        html = fromstring(result.content)
        try:
            token = html.xpath('//*[@name="csrf-token"]')[0].attrib['content']
            return token
        except Exception as err:
            pytest.fail(f"Failed authorisation :{err}")
