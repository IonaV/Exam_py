# https://replit.com/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os

from factory.new_user import User
from details.registration_page import Reg_page
from details.home_page import Home_page

my_user = User()
reg_page = Reg_page()
home_page = Home_page()
options = ChromeOptions()
foptions = FirefoxOptions()
# True Запуск теста без включения браузера
options.headless = False

path = f'{os.getcwd()}/drivers/chromedriver'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
url = 'https://replit.com/'

driver.maximize_window()
driver.get(url)

# Переход на форму регистрации
home_page.enter_button(driver)

# Регистрация ползователя
# Заполнение поля Username
reg_page.username_field(driver, my_user.username)

# Заполнение поля Email
reg_page.email_field(driver, my_user.email)

# Заполнение поля Password
reg_page.password_field(driver, my_user.password)

# Кнопка зарегестрироваться
reg_page.register_button(driver)

driver.close()
