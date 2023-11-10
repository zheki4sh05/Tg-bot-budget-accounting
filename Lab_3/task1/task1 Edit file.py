# Создать программный файл F1 в текстовом формате, записать в него
# построчно данные, вводимые пользователем. Об окончании ввода данных
# будет свидетельствовать пустая строка. Скопировать из файла F1 в файл F2
# строки, начиная с N до K. Подсчитать количество согласных букв в файле F2
alfs = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'x', 'z']
print("Введите текст (конец - пустая строка):")
user_input = []
while True:
    row = input()
    if row != '':
        user_input.append(row + "\n")
    else:
        break
file_f1 = None
try:
    file_f1 = open("F1.txt", "a")
    file_f1.write("".join(user_input))
except IOError:
    print("Ошибка открытия файла F1!")
finally:
    file_f1.close()
from_index = 0
to_index = 0
print("Введите интервал для копирования строк")
while True:
    from_index = input("Скопировать с: ")
    to_index = input("До:")
    if from_index.isdigit() and to_index.isdigit():
        from_index = int(from_index)
        to_index = int(to_index)
        if from_index > to_index or from_index == 0 or to_index == 0:
            print("Неверно задан интервал!")
        else:
            break
    else:
        print("Нечисловой ввод!")
counter = 0
try:
    with open("F1.txt") as source, open("F2.txt", "a") as destination:
        copied_information = source.readlines()[from_index:(to_index+1)]
        for line in copied_information:
            for alf in line:
                if alf in alfs:
                    counter += 1
        print(f'Информация во втором файле:')
        for line in copied_information:
            print(line,end='')
        destination.write("".join(copied_information))
except IOError:
    print("Ошибка открытия файла!")
print(f'Кол-во согласных букв {counter}')
