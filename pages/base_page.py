from data import ELEMENT_LOAD_SECONDS
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):
        self.browser =browser

    def wait(self):
        return WW(self.browser, ELEMENT_LOAD_SECONDS)

    def find(self, by_locator):
        return self.wait().until(EC.presence_of_element_located(by_locator))


