import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions


from factory.new_user import User
from details.registration_page import Reg_page
from details.home_page import Home_page
from xpath.registration_page import xpath_error_email


def registration_unvalid_field_email():
    home_page = Home_page()
    chrome_options = ChromeOptions()
    chrome_options.headless = True
    path = f"{os.getcwd()}/drivers/chromedriver"
    service = Service(executable_path=path)
    url = 'https://replit.com/'
    my_user = User()
    reg_page = Reg_page()
    invalid_email = ['assd@', 'amsjdu@dkcj', 'amsjdu@dkcj.', "@dkcj.com", "amsjdu@@dkcj.com", 'amsjdu@dkcj..com', 'amsjd u@dkcj.com']

    with webdriver.Chrome(service=service, options=chrome_options) as driver:
        driver.maximize_window()
        driver.get(url)
        home_page.enter_button(driver)
        for mail in invalid_email:
            reg_page.email_field(driver, mail)
            error_email = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(('xpath', xpath_error_email)))
            if error_email.is_enabled() == 'true':
                a = 'false'
                break
            else:
                a = 'true'

    return a, 'true'


if __name__ == '__main__':
    registration_unvalid_field_email()
