from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class HomePage(BasePage):

    LOGIN_BUTTON = (By.XPATH, '//button[@class="btn btn-primary btn-lg"]')
    DROPDOWN = (By.ID, 'userSelect')
    LOG_BTN = (By.XPATH, '//button[@type="submit"]')
    CONFIRM_ELEMENT = (By.XPATH, '//span[text()="Harry Potter"]')
    HOME_BUTTON = (By.XPATH, '//button[@class="btn home"]')


    def go_to_home_page(self):
        self.find(self.HOME_BUTTON).click()


    def do_login(self):
        self.find(self.LOGIN_BUTTON).click()


    def select_name(self):
        dropdown = self.find(self.DROPDOWN)
        dropdown.click()
        se = Select(dropdown)
        for item in se.options:
            if item.text == 'Harry Potter':
                item.click()
                break


    def login_submit(self):
        self.find(self.LOG_BTN).click()