# Придумать класс самостоятельно, реализовать в нем методы экземпляра
# класса, статические, методы, методы класса.
from datetime import date


class User:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_user_name(self):
        return self.__name

    def get_user_surname(self):
        return self.__surname

    def get_user_age(self):
        return self.__age

    @classmethod
    def get_instance(cls, name, surname, year):
        return cls(name, surname, date.today().year - year)

    @staticmethod
    def is_adult(age):
        return age >= 18


user_1 = User("John", "Smith", 18)
user_2 = User.get_instance("Tom", "Brown", 1989)

if User.is_adult(user_1.get_user_age()):
    print(f'Пользователь {user_1.get_user_name()} уже совершеннолетний')

print(f'Пользователь {user_2.get_user_name()} {user_2.get_user_surname()} зарегистрировался!')
