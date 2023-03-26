import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions


from factory.new_user import User
from details.registration_page import Reg_page
from details.home_page import Home_page
from xpath.registration_page import xpath_register_buttons_create


def registration_with_empty_field_username():
    home_page = Home_page()
    chrome_options = ChromeOptions()
    chrome_options.headless = True
    path = f"{os.getcwd()}/drivers/chromedriver"
    service = Service(executable_path=path)
    url = 'https://replit.com/'
    my_user = User()
    reg_page = Reg_page()

    with webdriver.Chrome(service=service, options=chrome_options) as driver:
        driver.maximize_window()
        driver.get(url)
        home_page.enter_button(driver)
        reg_page.email_field(driver, my_user.email)
        reg_page.password_field(driver, my_user.password)
        register_buttons_create = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(('xpath', xpath_register_buttons_create)))
        if register_buttons_create.is_enabled() == 'false':
            a = 'true'
        else:
            a = 'false'

    return a, 'false'


if __name__ == '__main__':
    registration_with_empty_field_username()
