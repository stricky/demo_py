from ..field_abstract import AbstractField


class EmailField(AbstractField):

    def __init__(self,
                 name='email address',
                 ):
        self.data_type_id = 144
        super(EmailField, self).__init__(name)
