# Создать вручную и заполнить несколькими строками текстовый
# файл, в котором каждая строка будет содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# ример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой
# компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт
# средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и
# их прибылями, а также словарь со средней прибылью. Если фирма получила
# убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий
# айл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit":
# 2000}]
import json

file_path_txt = "data.txt"
file_path_json="data.json"
result_list = [{}, {}]
average_incomes = []
try:
    with open(file_path_txt) as source:
        for line in source:
            firm_name, ownership, income, costs = line.split()
            earnings = float(income) - float(costs)
            result_list[0][firm_name] = earnings
            if earnings >= 0:
                average_incomes.append(earnings)
        result_list[1]["average_incomes"] = sum(list(map(lambda x: float(x), average_incomes))) / len(
                average_incomes)

except FileNotFoundError:
    print(f'Файл {file_path_txt} не найден!')
except IOError:
    print("Ошибка чтения файла")
try:
    with open(file_path_json, "w") as write_f:
        json.dump(result_list, write_f)
except IOError:
    print("Ошибка чтения файла!")

