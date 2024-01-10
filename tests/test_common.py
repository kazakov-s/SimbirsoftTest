import allure
from data import LOGIN_URL
from base_csv import do_csv
from pages.home_page import HomePage
from data import OPERATION_TYPE


class TestHomePage():

    @allure.suite("Финансовые операции")
    @allure.title('Проверка основных финансовых операций')
    @allure.description(
        f'Выполнение проверки зачисления и списание средств по счету клиента')
    @allure.tag('Common operations')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label('Developer', 'Sergey Kazakov')
    def test_operations(self, browser):
        browser.get(LOGIN_URL)
        self.page = HomePage(browser)
        self.page.do_login()
        self.page.select_name()
        self.page.login_submit()
        self.page.do_deposit()
        do_csv(OPERATION_TYPE[0], 0)
        self.page.do_withdrawal()
        self.page.confirm_deposit()
        self.page.confirm_transactions()
        do_csv(OPERATION_TYPE[1], 1)
        self.page.allure_attachment()
