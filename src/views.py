import json
from typing import Any, Dict

from src.reports import get_expenses_by_category
from src.services import analyze_cashback
from src.utils import (get_time_for_greeting,
                       get_data_time,
                       get_path_and_period,
                       get_card_with_spend, get_top_trans,
                       get_ccurent)


def main_info(date_time: str)->Dict[str, Any]:
    """hfdf"""
    greenting = get_time_for_greeting()
    time_period = get_data_time(date_time)
    sorted_df = get_path_and_period("../data/operations.xlsx", time_period)
    cards = get_card_with_spend(sorted_df)
    top_trans = get_top_trans(sorted_df,3)
    ccurent = get_ccurent("../data/user_settings.json")




    data ={
        "greeting": greenting,
        "cards": cards,
        "top_trans":top_trans,
        "ccurent":ccurent
    }
    json_date = json.dumps(data,ensure_ascii=False, indent =4)
    return json_date

def mai_per(date_time: str, gor:int, motheer:int)->Dict[str, Any]:

    ser = analyze_cashback(date_time,gor, motheer,3)

    data1 = {
        "ser":ser,
    }
    json_date1 = json.dumps(data1, ensure_ascii=False, indent=4)
    return json_date1

def new_main(transactions_df, category, date=None):
    reter = get_expenses_by_category(transactions_df, category,date)
    # formatted_output = {
    #     "category": category,
    #     "expenses": reter
    # }

    return reter
