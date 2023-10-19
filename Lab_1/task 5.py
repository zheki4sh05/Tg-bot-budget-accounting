# Реализуйте программу «Магазин автозапчастей», которая будет
# включать в себя шесть пунктов меню. У вас есть словарь, где ключ –
# название продукции. Значение – список, который содержит состав
# продукции, цену и кол-во (шт),которое есть в магазине.
# 1. Просмотр описания: название – описание
# 2. Просмотр цены: название – цена.
# 3. Просмотр количества: название – количество.
# 4. Всю информацию.
# 5. Покупка
# В пункте «Покупка» необходимо совершить покупку, с
# клавиатуры вводите название продукции и его кол-во, n – выход из
# программы. Посчитать цену выбранных товаров и сколько товаров
# осталось в изначальном списке
# 6. До свидания –

GET_DESC = 0
GET_PRICE = 1
GET_COUNT = 2

NOT_EXIST_WARN_MSG = "Товар отсутствует!"

user_order_list = dict()

data = {
    "Масло": [
        "75-85% базовые масла 10-20% Пакет присадок / добавок 5-10% Модификаторы вязкости",
        "23.5",
        "10"
    ],
    "Резина": [
        "зимние, для легковых автомобилей/минивенов и кроссоверов, без шипов, страна производства: Китай",
        "40",
        "40"
    ]
}


def get_value_from_dict(dictionary, key, data_type, error_msg):
    result = dictionary.get(key)
    if result:
        return result[data_type]
    else:
        return error_msg


def data_receiving_interface(data_type, message):
    while True:
        user_input = input("Введите название (0-Назад): ")
        if user_input != "0":
            print(f'{message} {get_value_from_dict(data, user_input, data_type, NOT_EXIST_WARN_MSG)}')
        elif user_input == "0":
            break


def show_data_in_table(data_dict):
    keys_list = sorted(data_dict.keys())
    for name in keys_list:
        result = data_dict.get(name)
        print(f'{name}  '
              f'{result[GET_PRICE]}$  '
              f'{result[GET_COUNT]} шт. '
              f'{result[GET_DESC]}  ')


def calc_total_price(user_data):
    total_price = 0
    for key in user_data.values():
        total_price += float(key[GET_PRICE] * key[GET_COUNT])
    return total_price


def create_order():
    while True:
        try:
            user_input = input("Введите название (0-назад): ")
            if user_input == "0":
                break
            count = int(get_value_from_dict(data, user_input, GET_COUNT, "0"))
            if count == 0:
                print(NOT_EXIST_WARN_MSG)
            else:
                while True:
                    user_count = int(input("Кол-во: "))
                    if user_count > count:
                        print(f'На складе {count} шт. Вы ввели {user_count}')
                    else:
                        price = float(get_value_from_dict(data, user_input, GET_PRICE, ""))
                        user_order_list[user_input] = ["", price, user_count]
                        price *= user_count
                        print(f'Итого: {str(price)}$')
                        data[user_input][GET_COUNT] = str(count - user_count)
                        print(f'Остаток на складе:   {data[user_input][GET_COUNT]}шт.')
                        break
        except ValueError:
            print("Неверный ввод!")
    print("----------------------------")
    show_data_in_table(user_order_list)
    print("----------------------------")
    print(f'Итоговая сумма$: {calc_total_price(user_order_list)}')
    print("----------------------------")
    user_order_list.clear()


def create_item():
    while True:
        item_name = input("Наименование (0-назад): ")
        if item_name == "0":
            break
        else:
            item_count = input("Кол-во: ")
            item_price = input("Цена: ")
            item_desc = input("Описание: ")
            data[item_name] = [item_desc, item_price, item_count]
            print("Добавлено")
            break


def show_menu():
    print("------------------------------------")
    print("| Система управления автомагазином |")
    print("------------------------------------")
    print("1 - Открыть описание")
    print("2 - Узнать цену")
    print("3 - Узнать кол-во")
    print("4 - Вся информация")
    print("5 - Оформить покупку")
    print("6 - Добавить товар")
    print("0 - Выход")


while True:
    show_menu()
    choice = input()
    if choice == "1":
        data_receiving_interface(GET_DESC, "Описание: ")
    elif choice == "2":
        data_receiving_interface(GET_PRICE, "Цена за шт.$: ")
    elif choice == "3":
        data_receiving_interface(GET_COUNT, "Остаток на складе : ")
    elif choice == "4":
        show_data_in_table(data)
    elif choice == "5":
        create_order()
    elif choice == "6":
        create_item()
    elif choice == "0":
        break
    else:
        print("Неверный ввод!")
