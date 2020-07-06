from source.items.field.field_abstract import AbstractField


class FieldsCollection:
    def __init__(self) -> None:
        self.collection = []

    def add_item(self, item: AbstractField):
        item.set_position(len(self.collection))
        self.collection.append(item)
