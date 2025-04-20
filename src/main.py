from src.utils import calculate_cashback, tabl_ger, get_time_for_greeting, top_transactions
from src.views import main_info

if __name__ == "__main__":
    print(main_info("2018-05-20 15:30:00"))

    print(get_time_for_greeting())
    for card in tabl_ger:
        cashback = calculate_cashback(card['total_spent'])
        print(
            f"Карта: **** **** **** {card['last_digits']}, Общая сумма расходов: {card['total_spent']} руб., Кешбэк: {cashback} руб.")

    print("\nТоп-5 транзакций:")
    for transaction in top_transactions:
        print(f"Сумма: {transaction['amount']} руб., Описание: {transaction['description']}")

    print("\nКурс валют:")
    for currency, rate in tabl_ger():
        print(f"{currency}: {rate:.2f} руб.")

    print("\nСтоимость акций S&P500:")
    for stock, price in tabl_ger():
        print(f"{stock}: {price:.2f} руб.")