import os
import datetime
import pandas as pd
from pathlib import Path
from data import fib_number

def do_csv(type, index):
    filepath = Path('report/out.csv')
    filepath.parent.mkdir(parents=True, exist_ok=True)
    date = datetime.datetime.now().strftime('%d %m %Y')+' '+datetime.datetime.now().strftime('%H:%M:%S')
    df = pd.DataFrame({'date': date,
                       'amount': fib_number,
                       'type': type}, index=[index])

    df.to_csv(filepath, encoding='utf-8', mode='a', index= False , header= False)