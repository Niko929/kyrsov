import pandas as pd
import json

def analyze_cashback(data_ser, year2, month2, top:int):
    # Чтение данных из Excel файла
    top_per = []
    df = pd.read_excel(data_ser, sheet_name = "Отчет по операциям")

    # Преобразуем столбец с датами в формат datetime
    df['Дата платежа'] = pd.to_datetime(df['Дата платежа'], dayfirst = True)

    # Фильтруем данные по указанному году и месяцу
    filtered_data = df[(df['Дата платежа'].dt.year == year2) & (df['Дата платежа'].dt.month == month2)]

    # Группируем данные по категориям и суммируем транзакции
    #cashback_analysis = filtered_data.groupby('Категория')['Сумма платежа'].sum().to_dict()

    # Преобразуем результат в JSON
   # result_json = json.dumps(cashback_analysis, ensure_ascii=False)

    top_tran = filtered_data.head(top)
    top_tran_sor = top_tran[
        [
            "Сумма платежа"
        ]

    ]
    for g1, j1 in top_tran_sor.iterrows():
        j1 = {
            "category1": f"{j1["Сумма платежа"]}"

        }
        top_per.append(j1)

    return top_per



