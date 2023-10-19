# Найдите наименьший четный элемент кортежа. Если такого нет,
# то выведите первый элемент
print("Вводите числа:")
numbers = []
counter = 1
while True:
    number = input(f'a{counter}=')
    if not number.isdigit():
        print("Неверный ввод!")
    elif number == "0":
        break
    else:
        numbers.append(int(number))
        counter += 1
if len(numbers) > 0:
    numbers_tuple = tuple(numbers)
    has_min_number = False
    min_number = numbers_tuple[0]
    i = 0
    while i < len(numbers_tuple):
        if numbers_tuple[i] % 2 == 0:
            has_min_number = True
            if numbers_tuple[i] < min_number:
                min_number = numbers_tuple[i]
        i += 1
    if has_min_number:
        print(f'Кортеж: {numbers_tuple}')
        print(f'Наименьший чётный элемент кортежа: {min_number}')
    else:
        print(f'Первый элемент кортежа: {numbers_tuple[0]}')

