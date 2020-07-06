from abc import ABCMeta, abstractmethod
from typing import List


class AbstractMapper:
    __metaclass__ = ABCMeta

    schema: List[tuple]

    def serialize(self):
        response = []
        schema = self.schema
        for item in schema:
            response.append(self._convert_field(item))
        return response

    @staticmethod
    def _build_boolean_field(key: str, value: bool) -> List[tuple]:
        res = [(key, 0)]
        if value:
            res.append((key, 1))
        return res

    @abstractmethod
    def _convert_field(self, item):
        pass
