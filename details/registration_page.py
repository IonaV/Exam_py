from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from xpath.registration_page import (
    xpath_register_username,
    xpath_register_email,
    xpath_register_password,
    xpath_register_buttons_create,
    xpath_user_finish)


class Reg_page:
    TIMEOUT = 30

    def email_field(self, driver, email):
        register_email = WebDriverWait(driver, self.TIMEOUT).until(
            EC.presence_of_element_located(('xpath', xpath_register_email)))
        register_email.send_keys(email)

    def username_field(self, driver, username):
        register_username = WebDriverWait(driver, self.TIMEOUT).until(
            EC.presence_of_element_located(('xpath', xpath_register_username)))
        register_username.send_keys(username)

    def password_field(self, driver, password):
        register_password = WebDriverWait(driver, self.TIMEOUT).until(
            EC.presence_of_element_located(('xpath', xpath_register_password)))
        register_password.send_keys(password)

    def register_button(self, driver):
        register_buttons_create = WebDriverWait(driver, self.TIMEOUT).until(
            EC.presence_of_element_located(('xpath', xpath_register_buttons_create)))
        register_buttons_create.click()

    def finish_register(self, driver):
        login_textarea = WebDriverWait(driver, self.TIMEOUT).until(
            EC.presence_of_element_located(('xpath', xpath_user_finish)))
        login = login_textarea.text
        return login

    def get_registered_username(self, driver):
        try:
            login_textarea = WebDriverWait(driver, self.TIMEOUT).until(
                EC.presence_of_element_located(('xpath', xpath_user_finish)))
            return login_textarea.text
        except TimeoutException:
            print("Failed to get registered username. Timeout occurred.")
            return None
