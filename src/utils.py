from datetime import datetime

import pandas as pd
from pandas import DataFrame
import requests

def get_time_for_greeting():
    """Функция возращает приветсивие, в зависимости от времени"""
    user_datetime = datetime.now().hour
    if 5 <= user_datetime < 12:
        return "Доброе утро"
    elif 12<= user_datetime < 18:
        return "Добрый дeнь"
    elif 18<=  user_datetime < 22:
        return "Добрый вечер"
    else:
        return "Добрый день"

def get_data_time(date_time: str, date_format:str = "%Y-%m-%d %H:%M:%S") -> list[str]:
    dt = datetime.strptime(date_time,date_format)
    start_of_month = dt.replace(day = 1)

    return [
        start_of_month.strftime("%d.%m.%Y %H:%M:%S"),
        dt.strftime("%d.%m.%Y %H:%M:%S")
    ]

def calculate_cashback(total_spent):
    return total_spent // 100

def tabl_ger(her="../data/operations.xlsx"):
    excel_data = pd.read_excel(her)
    excel_data_dict = excel_data.to_dict(orient="records")
    return excel_data_dict

top_transactions = sorted(tabl_ger, key=lambda x: x['amount'], reverse=True)[:5]



