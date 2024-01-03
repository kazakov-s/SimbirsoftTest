from data import LOGIN_URL
from time import sleep
from pages.login_page import HomePage

class TestHomePage():

    def test_get(self, browser):
        browser.get(LOGIN_URL)
        sleep(1)


    def test_auth(self, browser):
        self.page = HomePage(browser)
        self.page.go_to_home_page()
        sleep(1)

        self.page.do_login()
        self.page.select_name()
        self.page.login_submit()
        sleep(1)