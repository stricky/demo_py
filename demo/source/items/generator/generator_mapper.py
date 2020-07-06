from source.items.abstract.abstract_mapper import AbstractMapper
from source.items.field.fields_collection import FieldsCollection
from source.API.api import API, Request
from ..generator_constants import GeneratorConstants as constants


class GeneratorMapper(AbstractMapper):
    def __init__(self,
                 api: API,
                 fields: FieldsCollection,
                 format_type: str,
                 rows_count: int,
                 line_ending: str,
                 is_headers: bool,
                 is_bom: bool):
        self.api = api
        self.fields = fields
        self.format = format_type
        self.rows_count = rows_count
        self.line_ending = line_ending
        self.is_header = is_headers
        self.is_bom = is_bom

        assert format_type in constants.DATA_TYPES, 'Wrong data type in input'
        assert line_ending in constants.LINE_ENDINGS, 'Wrong Line Ending in input'
        self.schema = [
            ("project_id", None),
            ('id', None),
            ('num_rows', self.rows_count),
            ('file_format', self.format),
            ('line_ending', self.line_ending),

            ('table_name', "MOCK_DATA"),
            ('include_create_sql', 0),
            ('array', 0),
            ('array', 1),
            ('include_nulls', 0),
            ('include_nulls', 1),
            ('delimiter', ','),
            ('quote_char', '"'),
            ('xml_root_element', 'dataset'),
            ('xml_record_element', 'record'),
            ('name', None)
        ]
        self.schema + self._build_boolean_field('bom', self.is_bom)
        self.schema + self._build_boolean_field('include_header', self.is_header)

    def download(self):
        request = self._build_request()
        request.add_data([("preview", False)])
        r = self.api.post('schemas/download', request)
        return r

    def preview(self):
        request = self._build_request()
        request.add_data([("preview", True)])
        r = self.api.post('schemas/download', request)
        return r

    def _build_request(self) -> Request:
        request = Request()
        request.add_data(self.serialize())
        for field in self.fields.collection:
            request.add_data(field.mapper.serialize())
        return request

    def _convert_field(self, item: tuple) -> tuple:
        list_item = list(item)
        res = (f"schema[{list_item[0]}]", list_item[1])
        return res
