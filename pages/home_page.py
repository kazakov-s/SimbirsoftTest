from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from data import fib_number
from pages.base_page import BasePage
from time import sleep
from pathlib import Path
import allure


class HomePage(BasePage):
    LOGIN_BUTTON = (By.XPATH, '//button[@class="btn btn-primary btn-lg"]')
    DROPDOWN = (By.ID, 'userSelect')
    LOG_BTN = (By.XPATH, '//button[@type="submit"]')
    CONFIRM_ELEMENT = (By.XPATH, '//span[text()="Harry Potter"]')
    HOME_BUTTON = (By.XPATH, '//button[@class="btn home"]')
    DEPOSIT_BUTTON = (By.XPATH, '//button[@ng-class="btnClass2"]')
    AMOUNT_INPUT = (By.XPATH, '//input[@type="number"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit"]')
    WITHDRAWAL_BUTTON = (By.XPATH, '//button[@ng-class="btnClass3"]')
    TRANSACTIONS_BUTTON = (By.XPATH, '//button[@ng-class="btnClass1"]')
    BALANCE = (By.XPATH, '//strong[text()="0"]')
    CREDIT = (By.XPATH, '//td[text()="Credit"]')
    DEBIT = (By.XPATH, '//td[text()="Debit"]')

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

    def do_deposit(self):
        self.find(self.DEPOSIT_BUTTON).click()
        self.find(self.AMOUNT_INPUT).send_keys(fib_number)
        self.find(self.SUBMIT_BUTTON).click()

    def do_withdrawal(self):
        self.find(self.WITHDRAWAL_BUTTON).click()
        sleep(1)
        self.find(self.AMOUNT_INPUT).send_keys(fib_number)
        self.find(self.SUBMIT_BUTTON).click()

    def confirm_deposit(self):
        deposit = self.find(self.BALANCE).text
        assert int(deposit) == 0, 'Ошибка, депозит не равен 0.'
        sleep(1)

    def confirm_transactions(self):
        self.find(self.TRANSACTIONS_BUTTON).click()
        assert self.find(self.CREDIT), 'Ошибка зачисления'
        assert self.find(self.DEBIT), 'Ошибка списания'

    def allure_attachment(self):
        filepath = Path('report/out.csv')
        allure.attach.file(filepath, attachment_type=allure.attachment_type.CSV)
