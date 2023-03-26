from registration_form_elements.buttons_create_size_height import get_register_buttons_height
from registration_form_elements.buttons_create_size_width import get_register_buttons_width
from registration_form_elements.email_input_size_height import get_email_input_height
from registration_form_elements.email_input_size_width import get_email_input_width
from registration_form_elements.password_input_size_height import get_password_input_height
from registration_form_elements.password_input_size_width import get_password_input_width
from registration_form_elements.username_input_size_height import get_username_input_height
from registration_form_elements.username_input_size_width import get_username_input_width


def test_get_register_buttons_height():
    a = get_register_buttons_height()
    assert a[0] == a[1]


def test_get_register_buttons_width():
    a = get_register_buttons_width()
    assert a[0] == a[1]


def test_get_email_input_height():
    a = get_email_input_height()
    assert a[0] == a[1]


def test_get_email_input_width():
    a = get_email_input_width()
    assert a[0] == a[1]


def test_get_password_input_height():
    a = get_password_input_height()
    assert a[0] == a[1]


def test_get_password_input_width():
    a = get_password_input_width()
    assert a[0] == a[1]


def test_get_username_input_height():
    a = get_username_input_height()
    assert a[0] == a[1]


def test_get_username_input_width():
    a = get_username_input_width()
    assert a[0] == a[1]
