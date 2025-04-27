from src.views import mai_per, main_info, new_main

if __name__ == "__main__":
    print(main_info("2018-05-20 15:30:00"))
    print(mai_per("../data/operations.xlsx", 2019 , 10))
    print(new_main("../data/operations.xlsx", 'Пополнения', '2019-01-01'))

