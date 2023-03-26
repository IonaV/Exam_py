import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions


from factory.new_user import User
from details.registration_page import Reg_page
from details.home_page import Home_page
from xpath.registration_page import xpath_error_password


def registration_unvalid_field_password():
    home_page = Home_page()
    chrome_options = ChromeOptions()
    chrome_options.headless = True
    path = f"{os.getcwd()}/drivers/chromedriver"
    service = Service(executable_path=path)
    url = 'https://replit.com/'
    my_user = User()
    reg_page = Reg_page()
    invalid_password = ['1qwe3', 'asdef acec', '        ']

    with webdriver.Chrome(service=service, options=chrome_options) as driver:
        driver.maximize_window()
        driver.get(url)
        home_page.enter_button(driver)
        for password in invalid_password:
            reg_page.password_field(driver, password)
            error_password = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(('xpath', xpath_error_password)))
            if error_password.is_enabled() == 'true':
                a = 'false'
            else:
                a = 'true'

    return a, 'true'


if __name__ == '__main__':
    registration_unvalid_field_password()
