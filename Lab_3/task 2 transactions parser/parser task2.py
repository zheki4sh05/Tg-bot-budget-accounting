# Имеется текстовый файл «Клиент банка», строка которого содержит
# в себе информацию: фамилия клиента, сумма на счете, дата последнего
# изменения.
# Вывести на экран все фамилии, сумма на счету которых больше 1000.
# Определить клиентов, с максимальной суммой на счету. Файл заполнить
# заранее (не программно).
# Пример файла:
# Иванов 120 12.09.2022
# Петров 0 15.08.2022
from operator import itemgetter
MIN_BALANCE = 1000
users_list = []
max_user_balance = 0
most_rich_user = ""
try:
    with open("database.txt", "r") as source:
        for line in source:
            surname, balance, date = line.split()
            balance = int(balance)
            if balance > MIN_BALANCE:
                print(f'Имя {surname} Дата изм.:{date}')
            users_list.append([surname, balance, date])
except IOError as error:
    print(error)
most_rich_user = max(users_list, key=itemgetter(1))
print(f'Самый богатый клиент: {most_rich_user[0]}. Баланс: {most_rich_user[1]}Byn. Дата изм. {most_rich_user[2]}')
