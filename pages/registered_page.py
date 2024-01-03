from selenium.webdriver.common.by import By
from data import fib_number
from pathlib import Path
from pages.base_page import BasePage
from time import sleep
import allure

class RegisteredPage(BasePage):

    DEPOSIT_BUTTON = (By.XPATH, '//button[@ng-class="btnClass2"]')
    AMOUNT_INPUT = (By.XPATH, '//input[@type="number"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit"]')
    WITHDRAWAL_BUTTON = (By.XPATH, '//button[@ng-class="btnClass3"]')
    TRANSACTIONS_BUTTON = (By.XPATH, '//button[@ng-class="btnClass1"]')
    BALANCE = (By.XPATH, '//strong[text()="0"]')
    CREDIT = (By.XPATH, '//td[text()="Credit"]')
    DEBIT = (By.XPATH, '//td[text()="Credit"]')


    def do_deposit(self):
        self.find(self.DEPOSIT_BUTTON).click()
        self.find(self.AMOUNT_INPUT).click()
        self.find(self.AMOUNT_INPUT).send_keys(fib_number)
        self.find(self.SUBMIT_BUTTON).click()
        sleep(1)


    def do_withdrawal(self):
        self.find(self.WITHDRAWAL_BUTTON).click()
        self.find(self.AMOUNT_INPUT).click()
        sleep(1)
        self.find(self.AMOUNT_INPUT).send_keys(fib_number)
        sleep(1)
        self.find(self.SUBMIT_BUTTON).click()


    def confirm_deposit(self):
        deposit = self.find(self.BALANCE).text
        assert int(deposit) == 0, 'Ошибка депозит не равен 0.'
        sleep(1)


    def confirm_transactions(self):
        self.find(self.TRANSACTIONS_BUTTON).click()
        assert self.find(self.CREDIT), 'Ошибка зачисления'
        assert self.find(self.DEBIT), 'Ошибка списания'

    def allure_attachment(self):
        filepath = Path('report/out.csv')
        allure.attach.file(filepath, attachment_type=allure.attachment_type.CSV)
