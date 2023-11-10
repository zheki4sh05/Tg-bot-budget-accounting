# Класс Example. В нём пропишите 3 (метода) функции.
# Две переменные задайте статически, две динамически.
# Первый метод: создайте переменную и выведите её.
# Второй метод: верните сумму 2-ух глобальных переменных.
# Третий метод: верните результат возведения первой динамической
# переменной во вторую динамическую переменную.
# Создайте объект класса. Напечатайте оба метода. Напечатайте переменную a.

class Example:

    def __init__(self):
        Example.op1 = 2
        Example.op2 = 3

    def create_new_var_4(self,val1):
        self.op4 = val1
        return self.op4

    def create_new_var_5(self, val2):
        self.op5 = val2
        return self.op4

    def get_glob_sum(self):
        return self.op1 + self.op2

    def raise_val(self):
        Example.op1 = Example.op1 ** Example.op2
        return Example.op1


newExample = Example()
print(f'Сумма 2-ух глобальных переменных {newExample.get_glob_sum()}')
print(f'1 новая переменная {newExample.create_new_var_4(12)}')
print(f'2 новая переменная {newExample.create_new_var_4(15)}')
print(f'Возведение в степень {newExample.raise_val()}')
