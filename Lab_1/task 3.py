# Найдите сумму положительных элементов списка.
# Найдите сумму элементов списка между двумя первыми нулями. Если
# двух нулей нет в списке, то выведите ноль
while True:
    size_of_mass = input("Введите количество элементов в списке: ")
    if size_of_mass.isdigit():
        size_of_mass = int(size_of_mass)
        break
    else:
        print("Неверный ввод!")
print("Вводите числовые элементы: ")
mass = []
while True:
    has_mass = False
    try:
        mass = [float(input()) for i in range(size_of_mass)]
        has_mass = True
    except ValueError:
        print("Неверный ввод!")
    if has_mass:
        break
sum_of_positive = 0
for i in mass:
    if i > 0:
        sum_of_positive += i
first_zero_index = -1
second_zero_index = -1
if 0 in mass:
    first_zero_index = mass.index(0)
if 0 in mass[first_zero_index + 1:]:
    second_zero_index = mass.index(0, first_zero_index + 1)
print(f'Сумма положительных элементов: {sum_of_positive}')
if second_zero_index - first_zero_index == 2 or second_zero_index - first_zero_index == 1:
    print("Нули стоят рядом либо через один")
elif second_zero_index * first_zero_index < 0:
    print("Только один нулевой элемент")
elif second_zero_index < 0 and first_zero_index < 0:
    print("Нулей нет")
else:
    print(f'Сумма элементов, расположенных между нулями: {sum(mass[first_zero_index + 1:second_zero_index])}')