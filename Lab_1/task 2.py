# Посчитать, сколько пар (стоят рядом) верхнего и нижнего
# регистра находится в веденном с клавиатуры слове. (Пример HjkLM- 1
# пара нижнего, 1 пара верхнего), а также сколько всего букв в слове.
while True:
    input_string = input("Введите строку (0-exit): ")
    if input_string != "0":
        capital_pair_count = 0
        lower_capital_pair_count = 0
        for i in range(len(input_string) - 1):
            if input_string[i].islower() and input_string[i + 1].islower():
                lower_capital_pair_count += 1
            elif input_string[i].isupper() and input_string[i + 1].isupper():
                capital_pair_count += 1
        print(f'Букв в строке: {str(len(input_string))}\n'
              f'Кол-во пар верхнего регистра: {capital_pair_count}\n'
              f'Кол-во пар нижнего регистра: {str(lower_capital_pair_count)}')
    else:
        print("Завершение программы")
        break