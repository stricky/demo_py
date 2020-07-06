from ..field_abstract import AbstractField


class IPAddressField(AbstractField):
    def __init__(self,
                 name='ip_address',
                 ):
        self.data_type_id = 145
        super(IPAddressField, self).__init__(name)
