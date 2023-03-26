from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath.home_page import xpath_enter_button


class Home_page:
    def enter_button(self, driver, timeout=30):
        enter_button = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(('xpath', xpath_enter_button)))
        enter_button.click()
