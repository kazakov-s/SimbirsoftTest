from base_csv import do_csv
from pages.registered_page import RegisteredPage
from data import OPERATION_TYPE

class TestRegisteredPage():

    def test_deposit(self, browser):
        self.page = RegisteredPage(browser)
        self.page.do_deposit()
        do_csv(OPERATION_TYPE[0],0)


    def test_withdrawal(self, browser):
        self.page = RegisteredPage(browser)
        self.page.do_withdrawal()
        self.page.confirm_deposit()
        self.page.confirm_transactions()
        do_csv(OPERATION_TYPE[1],1)

