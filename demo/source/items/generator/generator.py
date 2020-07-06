from .generator_mapper import GeneratorMapper
from source.API.api import API
from source.items.field.fields_collection import FieldsCollection
from ..generator_constants import GeneratorConstants


class Generator:
    def __init__(self,
                 api: API,
                 fields: FieldsCollection,
                 format_type=GeneratorConstants.DATA_TYPE_CSV,
                 rows_count=1000,
                 line_ending=GeneratorConstants.LINE_ENDING_UNIX,
                 is_headers=True,
                 is_bom=False
                 ):
        self.api = api
        self.fields = fields
        self.format = format_type
        self.rows_count = rows_count
        self.line_ending = line_ending
        self.is_header = is_headers
        self.is_bom = is_bom
        self.mapper = GeneratorMapper(self.api,
                                      fields,
                                      format_type,
                                      rows_count,
                                      line_ending,
                                      is_headers,
                                      is_bom)

    def download(self):
        return self.mapper.download()

    def preview(self):
        return self.mapper.preview()
