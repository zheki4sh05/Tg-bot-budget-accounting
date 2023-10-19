my_dict = {"a": 1, "b": 2, "c": 3}
value_key='a'
try:
    if not value_key.isalpha():
        raise TypeError("Неверный тип данных ключа!")
    value = my_dict[value_key]
    print(f'Ключ: {value_key} Значение:{value}')
except KeyError:
    print("Такого ключа не существует!")
except TypeError as error:
    print(error)
finally:
    print("Программа завершена!")
