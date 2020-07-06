from abc import ABCMeta, abstractmethod, abstractproperty
from datetime import date
from source.items.field.field_mapper import FieldMapper


class AbstractField:
    __metaclass__ = ABCMeta

    data_type_id: int

    def __init__(self,
                 name: str,
                 is_active=True):
        self.position = 0
        self.name = name
        self.is_active = is_active
        current_date = date.today()
        self.data_max = current_date.strftime("%-d/%-m/%Y")
        self.data_min = current_date.replace(year=current_date.year - 1).strftime("%-d/%-m/%Y")
        self.data_format = '%-m/%-d/%Y'
        self.mapper = FieldMapper(self.name,
                                  self.is_active,
                                  self.data_type_id,
                                  self.position,
                                  self.data_max,
                                  self.data_min,
                                  self.data_format)

    def set_position(self, position: int):
        self.position = position
        self.mapper.position = position
