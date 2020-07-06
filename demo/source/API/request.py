from abc import ABCMeta
from typing import List


class Request:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.headers = {
            ('Content-Type', 'application/x-www-form-urlencoded')  # todo validate
        }

        self.data = [
            ("utf8", "✓"),
            ("provider", None),
        ]

    def add_data(self, schema: List[tuple]):
        self.data += schema

    def set_preview(self, preview: bool):
        self.add_data([('preview', preview)])
