import json
import pandas as pd
def process_card_data(date_time) :
    card_data = {}

    for transaction in date_time:
        card_number = transaction['card_number'][-4:]  # последние 4 цифры карты
        amount = transaction['amount']

        if card_number not in card_data:
            card_data[card_number] = {
                'total_spent': 0,
                'cashback': 0,
                'transactions': []
            }

        card_data[card_number]['total_spent'] += amount
        card_data[card_number]['cashback'] += amount // 100
        card_data[card_number]['transactions'].append(transaction)
    return card_data

ter = pd.read_excel("../data/operations.xlsx")
print(process_card_data(ter))