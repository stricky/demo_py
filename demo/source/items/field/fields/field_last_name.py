from ..field_abstract import AbstractField


class LastNameField(AbstractField):

    def __init__(self,
                 name='last_name'):
        self.data_type_id = 161
        super(LastNameField, self).__init__(name)
