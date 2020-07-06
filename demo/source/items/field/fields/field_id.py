from ..field_abstract import AbstractField


class IDField(AbstractField):

    def __init__(self,
                 name='id',
                 ):
        self.data_type_id = 140
        super(IDField, self).__init__(name)
