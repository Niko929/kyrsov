import pandas as pd
from datetime import datetime

def get_expenses_by_category(transactions_df, category, date=None):
    # Преобразуем столбец 'Дата платежа' в формат datetime
    df = pd.read_excel(transactions_df, sheet_name="Отчет по операциям")
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], dayfirst=True)

    # Если дата не передана, берем текущую дату
    if date is None:
        date = datetime.now()
    else:
        date = pd.to_datetime(date)

    # Вычисляем дату три месяца назад
    three_months_ago = date - pd.DateOffset(months=3)

    # Фильтруем датафрейм по категории и дате
    filtered_df = df[
        (df["Категория"] == category) &
        (df["Дата операции"] >= three_months_ago) &
        (df["Дата операции"] <= date)
    ]

    # Проверка результата фильтрации
    #print(filtered_df)  # Выводим отфильтрованные данные для отладки

    # Суммируем траты
    total_expenses = filtered_df["Сумма операции"].sum()

    return (filtered_df,
            total_expenses)




transactions_df = "../data/operations.xlsx"
result = get_expenses_by_category(transactions_df, 'Пополнения', '2019-01-01')  # Передаем дату в строковом формате
print(result)

