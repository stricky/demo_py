from pytest import fixture
from source.items.field.fields_collection import FieldsCollection
from source.items.field.fields.field_email import EmailField
from source.items.field.fields.field_id import IDField
from source.items.generator.generator import Generator
from source.API.response import Response
from .helpers.validators import Validators


@fixture()
def generated_data(api) -> Response:
    fields = FieldsCollection()
    fields.add_item(IDField('Row Number'))
    fields.add_item(EmailField())
    generator = Generator(api, fields, 'csv', 50)
    response = generator.download()
    return response


def test_is_valid_format(generated_data: Response):
    assert generated_data.content_type == 'csv'


def test_all_values_created(generated_data: Response):
    """
    Two additional fields-header and last symbol
    """
    assert len(generated_data.content.get_content()) == 50 + 2, f"Failed to create {50} items for fields"


def test_all_fields_created(generated_data: Response):
    assert len(generated_data.content.get_content()[0]) == 2, f"Failed to create 2 fields"
    field1 = generated_data.content.get_content()[0][0]
    assert field1 == 'Row Number', f"Wrong name for Row Number field"


def test_row_content(generated_data: Response):
    source = generated_data.content.get_content()
    for i in range(1, 50):
        item = source[i]
        assert Validators.is_valid_id(item[0]), f"Row number is not a number {item[0]}"
        assert int(item[0]) == i, f"Wrong row numeration. Actual: {item[0]}, expected: {i}"


def test_email_content(generated_data: Response):
    source = generated_data.content.get_content()
    for i in range(1, 50):
        item = source[i]
        assert Validators.is_valid_mail(item[1]), f"Incorrect email was generated: {item[1]}"
