from ..field_abstract import AbstractField


class FirstNameField(AbstractField):

    def __init__(self,
                 name='first_name'):
        self.data_type_id = 159
        super(FirstNameField, self).__init__(name)
