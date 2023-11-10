# Класс Example. В нём пропишите 3 (метода) функции.
# Две переменные задайте статически, две динамически.
# Первый метод: создайте переменную и выведите её.
# Второй метод: верните сумму 2-ух глобальных переменных.
# Третий метод: верните результат возведения первой динамической
# переменной во вторую динамическую переменную.
# Создайте объект класса. Напечатайте оба метода. Напечатайте переменную a.

class Example:
    op1 = 2
    op2 = 3
    op3 = 4

    def create_new_var(self, val):
        self.op4 = val

    def get_glob_sum(self):
        return self.op1 + self.op2

    def raise_val(self):
        Example.op1 = Example.op1 ** Example.op2


newExample = Example()
newExample.create_new_var(12)
print(f'Новая переменная {newExample.op4}')
newExample.raise_val()
print(f'Возведение в степень {newExample.op1}')