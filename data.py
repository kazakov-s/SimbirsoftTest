import datetime
import configparser

config = configparser.ConfigParser()
config.read('data.ini')

EXEC_URL = config.get('DEFAULT', 'EXEC_URL')
ELEMENT_LOAD_SECONDS = config.get('DEFAULT', 'ELEMENT_LOAD_SECONDS')
LOGIN_URL = config.get('DEFAULT', 'LOGIN_URL')
REGISTERED_URL = config.get('DEFAULT', 'REGISTERED_URL')
OPERATION_TYPE = [config.get('DEFAULT', 'CREDIT_TYPE'), config.get('DEFAULT', 'DEBIT_TYPE')]


def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b


current_day = datetime.date.today().day
n = current_day + 1
fib_number = fibonacci(n)
