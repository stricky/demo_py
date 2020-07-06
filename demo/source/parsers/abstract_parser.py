from abc import ABCMeta, abstractmethod


class AbstractParser:
    __metaclass__ = ABCMeta

    def __init__(self, source):
        self._source = self._parse(source)

    @abstractmethod
    def _parse(self, source):
        pass

    @abstractmethod
    def is_loaded(self):
        pass

    def get_content(self):
        return self._source
