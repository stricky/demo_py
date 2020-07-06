from source.items.abstract.abstract_mapper import AbstractMapper


class FieldMapper(AbstractMapper):
    def __init__(self,
                 name: str,
                 is_active: bool,
                 data_type_id: int,
                 position,
                 data_max,
                 data_min,
                 data_format):
        self.position = position
        self.schema = [
            ("name", name),
            ("data_type_id", data_type_id),
            ("_destroy", is_active),  # or 1 if field will be removed

            ("sequence_start", 1),
            ("sequence_step", 1),
            ("sequence_repeat", 1),
            ("sequence_restart", None),
            ("min", 1),
            ("max", 100),

            ("decimal_places", 0),
            ("normal_dist_mean", 0),
            ("dist_probability", 0.5),
            ("dist_lambda", 1),
            ("normal_dist_sd", 1),
            ("normal_dist_decimals", 2),

            # options
            ("date_format", data_format),
            ("min_time", data_min),
            ("max_time", data_max),
            ("time_format", '%-l:%M %p'),

            ("values", None),
            ("min_words", 10),
            ("max_words", 20),
            ("min_paragraphs", 1),
            ("max_paragraphs", 3),
            ("min_sentences", 1),
            ("max_sentences", 10),
            ("expression", None),

            ("style", 'A-'),
            ("regex", None),
            ("min_money", 0),
            ("max_money", 10),
            ("money_symbol", '$'),
            ("formula", None),
            ("min_items", 1),
            ("max_items", 5),
            ("list_weights", None),
            ("list_selection_style", 'random'),
            ("only_us_places", 0),
            ("only_us_places", 1),
            ("states", None),
            ("file_type", 'common'),
            ("file_name_format", 'camel-caps'),
            ("sql_expression", None),
            ("countries", None),
            ("avatar_width", 50),
            ("avatar_height", 50),
            ("image_width_min", 100),
            ("image_height_min", 100),
            ("image_width_max", 250),
            ("image_height_max", 250),
            ("image_format", 'random'),
            ("phone_format", '###-###-####'),
            ("character_sequence_format", None),
            ("null_percentage", 0),
            ("advanced_formula", None)
        ]
        self._set_include_host()
        self._set_include_protocol()
        self._set_include_query_string()

    def _set_include_protocol(self, include_protocol=True):
        self.schema + self._build_boolean_field('include_protocol', include_protocol)

    def _set_include_host(self, include_host=True):
        self.schema + self._build_boolean_field('include_host', include_host)

    def _set_include_query_string(self, include_query_string=True):
        self.schema + self._build_boolean_field('include_query_string', include_query_string)

    def _convert_field(self, item: tuple) -> tuple:
        list_item = list(item)
        return tuple([f"schema[columns_attributes][{self.position}][{list_item[0]}]", list_item[1]])
