import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from data import EXEC_URL


@pytest.fixture(scope='package')
def browser():
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    driver = webdriver.Remote(command_executor=EXEC_URL, options=chr_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
