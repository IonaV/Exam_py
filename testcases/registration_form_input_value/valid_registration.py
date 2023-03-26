import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from factory.new_user import User
from details.registration_page import Reg_page
from details.home_page import Home_page


def valid_registration():
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
        reg_page.username_field(driver, my_user.username)
        reg_page.email_field(driver, my_user.email)
        reg_page.password_field(driver, my_user.password)
        reg_page.register_button(driver)
        a = reg_page.finish_register(driver)

    return a, 'How familiar are you with programming?'


if __name__ == '__main__':
    valid_registration()
