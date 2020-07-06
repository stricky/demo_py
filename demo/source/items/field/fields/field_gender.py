from ..field_abstract import AbstractField


class GenderField(AbstractField):

    def __init__(self,
                 name='gender',
                 ):
        self.data_type_id = 166
        super(GenderField, self).__init__(name)
