import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from details.home_page import Home_page
from xpath.registration_page import xpath_register_email


def get_email_input_width():
    home_page = Home_page()
    chrome_options = ChromeOptions()
    chrome_options.headless = True
    path = f"{os.getcwd()}/drivers/chromedriver"
    service = Service(executable_path=path)
    url = 'https://replit.com/'
    expected_width = 280

    with webdriver.Chrome(service=service, options=chrome_options) as driver:
        driver.maximize_window()
        driver.get(url)
        home_page.enter_button(driver)
        register_email = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(("xpath", xpath_register_email)))
        email_input_width = register_email.size["width"]

    return expected_width, email_input_width


if __name__ == '__main__':
    get_email_input_width()
