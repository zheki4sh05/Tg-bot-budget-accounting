# Дан двумерный массив и два числа: i и j. Поменяйте в массиве
# столбцы с номерами i и j и выведите результат.
# Программа получает на вход размеры массива n и m, затем элементы
# массива, затем числа i и j
from random import randint


def print_header(i1, i2,t1,t2):
    print("\t" * (i1), end='')
    print(t1, end='')
    print("\t" * (i2-i1), end='')
    print(t2)


def show_matrix(matrix):
    for row in matrix:
        for element in row:
            print(f'{element}\t', end='')
        print()


MIN_SIZE = 2
MAX_SIZE = 6
n = randint(MIN_SIZE, MAX_SIZE)  # rows
m = randint(n, MAX_SIZE)  # columns
i = 0
j = 0
while True:
    try:
        print(f'Введите номера столбцов (min: {1} max:{m}): ')
        i = int(input("i=")) - 1
        j = int(input("j=")) - 1
        if i > j:
            i, j = j, i
        elif i>=m or j>=m:
            raise IndexError("Неверный номер!")
        else:
            break
    except IndexError as error:
        print(error)
    except Exception:
        print("Неверный ввод!")
mass = []
for y in range(n):
    mass.append([randint(1, 10) for _ in range(m)])
print('Исходный массив:')
print_header(i,j,"->","<-")
show_matrix(mass)
print(f'Поменяем местами столбцы с номерами {i + 1} и {j + 1}')
for row in mass:
    row[i], row[j] = row[j], row[i]
print('Результат:')
print_header(i,j,"|<-","->|")
show_matrix(mass)
