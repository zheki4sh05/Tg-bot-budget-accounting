# Программа считывает число с консоли и выводит кол-во четных и нечётных чисел
while True:
    even_сount = 0
    not_even_count = 0
    number = input("Введите число (0-exit) : ")
    if number.isdigit():
        if int(number) != 0:
            for i in number:
                if int(i) % 2 == 0:
                    even_сount = even_сount + 1
                else:
                    not_even_count = not_even_count + 1
            print(f'Количество четных = {even_сount}\n'
                  f'Количество нечетных= {not_even_count}')
        else:
            break
    else:
        print("Неверный ввод!")
