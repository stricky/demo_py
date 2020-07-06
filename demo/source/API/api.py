import requests
from .session import Session
# from parsers import AbstractParser
from typing import List
from .request import Request
from .response import Response


class API:
    def __init__(self, session: Session):
        self.url = session.url
        self.data = [
            ("authenticity_token", session.csrf),
            ('utf', "✓"),
            ('provider', None),
        ]
        self.header = {
            'Content-type': 'application/x-www-form-urlencoded'
        }

        self.data = [("authenticity_token", session.csrf)]

    def post(self, method, input_request: Request):
        data = self.data + input_request.data

        result = requests.post(url=f"{self.url}/{method}", data=data, headers=self.header)
        assert result.status_code == 200, f"Actual API Response {result.status_code}"
        res = Response(result.content, result.headers['Content-type'])
        assert res.content.is_loaded(), 'Failed to load content'
        return res

    def build_data(self, params: List[tuple]):
        data = self.data + params
        content = "{%s}" % ', '.join("'%s': '%s'" % pair for pair in data)
        return content
