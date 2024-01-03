import allure
from base_csv import do_csv
from pages.registered_page import RegisteredPage
from data import OPERATION_TYPE


class TestRegisteredPage():

    def test_deposit(self, browser):
        self.page = RegisteredPage(browser)
        self.page.do_deposit()
        do_csv(OPERATION_TYPE[0],0)


    @allure.suite("Списание средств")
    @allure.title('Выполняем списание средств со счета')
    @allure.description(
        f'Выполняем списание средств со счета, проверяем правильность депозита и наличие транзакций в базе данных')
    @allure.tag('Debit')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.label('Developer', 'Sergey Kazakov')
    def test_withdrawal(self, browser):
        self.page = RegisteredPage(browser)
        self.page.do_withdrawal()
        self.page.confirm_deposit()
        self.page.confirm_transactions()
        do_csv(OPERATION_TYPE[1],1)
        self.page.allure_attachment()



