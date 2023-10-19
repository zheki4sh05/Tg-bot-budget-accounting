# Напишите функцию, которая будет принимать один аргумент. Если в
# функцию передаётся
# словарь - отсортировать в порядке возрастания и убывания по значению ключей
# список -  посчитать кол-во букв и чисел в нём.
# Число – определить простое, или нет
# Строка – вывести все слова палиндромы.
# Сделать проверку со всеми этими случаями.
def count_numbers_and_alfa(data):
    str_list = list(' '.join([str(item) for item in data]))
    numbers = ''
    counter_numb = 0
    counter_alfa = 0
    str_list.append('')
    for char in str_list:
        if char.isdigit():
            numbers += char
        if char != ' ' and not char.isdigit() and len(numbers) != 0:
            counter_numb += 1
            counter_alfa += 1
            numbers = ''
    return counter_numb, counter_alfa


def is_ordinary(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def sort_dict(user_dict):
    sorted_dict = dict(sorted(user_dict.items()))
    reversed_sorted_dict = dict(reversed(sorted_dict.items()))
    return sorted_dict, reversed_sorted_dict


def analyze(data):
    if isinstance(data, dict):
        return sort_dict(data)  # return tuple of 2 dict: 1 - sorted in ascending order,2 - sorted in descending order
    if isinstance(data, list):
        return count_numbers_and_alfa(data)  # return tuple of 2 elem: 1 - count of numbers, 2 - count of alfa
    if isinstance(data, int):
        return is_ordinary(data)  # return True or False ordinary number or not
    if isinstance(data, str):
        return [word for word in data.split(' ') if word == ''.join(reversed(word))]  # return list of palindrome words


DICT = 0
LIST = 1
NUMBER = 2
STR = 3

test_vars = [
    {"orange": "апельсин",
     "apple": "яблоко",
     "mango": "манго",
     "watermelon": "арбуз",
     "pineapple": "ананас",
     "banana": "банан",
     },
    ["u", 12, "24234"],
    11,
    "довод поляна шел шалаш солнце заказ"
]
result = analyze(test_vars[DICT])
print(f'По возрастанию: {result[0]}\nПо убыванию: {result[1]}\n')

result = analyze(test_vars[LIST])
print(f'Кол-во чисел: {result[0]}\nКол-во букв: {result[1]}\n')

result = analyze(test_vars[NUMBER])
print(f'Число {test_vars[NUMBER]} {"" if result else "не " }является простым\n')

result = analyze(test_vars[STR])
print(f'Слова палиндромы {result}')
