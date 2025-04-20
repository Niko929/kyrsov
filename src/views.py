import json
from typing import Any, Dict

from src.utils import get_time_for_greeting, get_data_time, get_path_and_period


def main_info(date_time: str)->Dict[str, Any]:
    """hfdf"""
    greenting = get_time_for_greeting()
    time_period = get_data_time(date_time)
    sorted_df = get_path_and_period("../data/operations.xlsx", time_period)
    print(time_period)

    data ={
        "greeting": greenting
    }
    json_date = json.dumps(data,ensure_ascii=False, indent =4)
    return json_date