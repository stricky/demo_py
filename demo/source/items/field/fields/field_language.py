from ..field_abstract import AbstractField


class LanguageField(AbstractField):

    def __init__(self,
                 name='language'):
        self.data_type_id = 167
        super(LanguageField, self).__init__(name)
