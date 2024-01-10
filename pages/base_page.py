from data import ELEMENT_LOAD_SECONDS
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def wait(self):
        return WW(self.browser, ELEMENT_LOAD_SECONDS)

    def find(self, by_locator):
        return self.wait().until(EC.element_to_be_clickable(by_locator))
