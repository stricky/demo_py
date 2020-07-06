from ..field_abstract import AbstractField
from source.items.generator_constants import GeneratorConstants


class DatetimeField(AbstractField):
    def __init__(self,
                 name='datetime'):
        self.data_type_id = 131
        super(DatetimeField, self).__init__(name)

    def set_min_max(self, min_date, max_date):
        self.data_min = min_date
        self.data_max = max_date

    def set_data_format(self, data_format: str):
        assert data_format in GeneratorConstants.DATA_FORMATS, 'Wrong data format'
        self.data_format = data_format
