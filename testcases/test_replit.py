from registration_form_input_value.valid_registration import valid_registration
from registration_form_input_value.registration_with_empty_field_username import registration_with_empty_field_username
from registration_form_input_value.registration_with_empty_field_email import registration_with_empty_field_email
from registration_form_input_value.registration_with_empty_field_password import registration_with_empty_field_password
from registration_form_input_value.registration_with_all_empty_field import registration_with_all_empty_field
from registration_form_input_value.registration_unvalid_field_username import registration_unvalid_field_username
from registration_form_input_value.registration_unvalid_field_email import registration_unvalid_field_email
from registration_form_input_value.registration_unvalid_field_password import registration_unvalid_field_password


def test_valid_registration():
    a = valid_registration()
    assert a[0] == a[1]


def test_registration_with_empty_field_username():
    a = registration_with_empty_field_username()
    assert a[0] == a[1]


def test_registration_with_empty_field_email():
    a = registration_with_empty_field_email()
    assert a[0] == a[1]


def test_registration_with_empty_field_password():
    a = registration_with_empty_field_password()
    assert a[0] == a[1]


def test_registration_with_all_empty_field():
    a = registration_with_all_empty_field()
    assert a[0] == a[1]


def test_registration_unvalid_field_username():
    a = registration_unvalid_field_username()
    assert a[0] == a[1]


def test_registration_unvalid_field_email():
    a = registration_unvalid_field_email()
    assert a[0] == a[1]


def test_registration_unvalid_field_password():
    a = registration_unvalid_field_password()
    assert a[0] == a[1]
