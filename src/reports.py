import pandas as pd
from datetime import datetime

def get_expenses_by_category(transactions_df, category, date=None):
    # Преобразуем столбец 'Дата платежа' в формат datetime
    transactions_df['Дата платежа'] = pd.to_datetime(transactions_df['Дата платежа'], dayfirst=True)

    # Если дата не передана, берем текущую дату
    if date is None:
        date = datetime.now()
    else:
        date = pd.to_datetime(date)

    # Вычисляем дату три месяца назад
    three_months_ago = date - pd.DateOffset(months=3)

    # Фильтруем датафрейм по категории и дате
    filtered_df = transactions_df[
        (transactions_df['Категория'] == category) &
        (transactions_df['Дата платежа'] >= three_months_ago) &
        (transactions_df['Дата платежа'] <= date)
    ]

    # Проверка результата фильтрации
    print(filtered_df)  # Выводим отфильтрованные данные для отладки

    # Суммируем траты
    total_expenses = filtered_df['Сумма операции'].sum()

    return  total_expenses



# Пример использования
# transactions_df = pd.read_excel("../data/operations.xlsx")
# result = get_expenses_by_category(transactions_df, 'Пополнения', '2019-01-01')  # Передаем дату в строковом формате
# print(result)
#
