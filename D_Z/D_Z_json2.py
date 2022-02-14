import json

data_base = {'Россия': 'Москва', 'Беларусь': 'Минск', 'Бразилия': 'Бразилиа', }


def intro():
    print("Выберите номер действия:\n1: добавление данных \n2 удаление данных \n3: поиск данных \
            \n4: редактирование страны \n5: просмотр данных \n6: сохранить данные и завершение работы \n ")
    x = (int(input("=>")))

    if x == 1:
        add_data()
    if x == 2:
        del_data()
    if x == 3:
        search()
    if x == 4:
        chenge()
    if x == 5:
        print_data()
    if x == 6:
        save_exit()


def add_data():  # 1
    country = str(input("вветите страну:"))
    city = str(input("введите город:"))
    if country in data_base:
        print(country, "такая страна уже есть!\n")
    else:
        data_base[country] = city
        print(country, city, "внесены в базу\n")
    intro()


def del_data():  # 2
    country = str(input("вветите страну, которую хотите удалить:"))
    try:
        data_base.pop(country)
    except KeyError:
        print(country, "станы в базе нет\n")
        intro()

    print(country, "удалена из базы\n")
    intro()


def search(): #3
    x = str(input("введите для поиска название страны или города"))
    for k, v in data_base.items():
        if k.lower() == x.lower():
            print(f"{k}: {v}")
        if v.lower() == x.lower():
            print(f"{k}: {v}")
    intro()


def chenge():  # 4
    new_country = str(input("вветите новую страну:"))
    country = str(input("вветите страну которую хотите заменить:"))
    try:
        data_base[new_country] = data_base.pop(country)
    except KeyError:
        print(country, "в базе нет")
    intro()


def print_data():  # 5
    for k, v in data_base.items():
        print(f"{k}: {v}")
    print()
    intro()


def save_exit():
    try:
        data = json.load(open("country_city.json"))
    except FileNotFoundError:
        data = []
    data.append(data_base)
    with open("country_city.json", "w") as f:
        json.dump(data, f,  indent=2, ensure_ascii=False)


intro()
