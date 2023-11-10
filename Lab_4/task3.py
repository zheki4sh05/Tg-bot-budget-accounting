# 1. Реализуйте базовый класс Car.
# 2. У класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# 3. Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
# PoliceCar;
# 4. Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля;
# 5. Для классов TownCar и WorkCar переопределите метод show_speed. При
# значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.

class Car:
    def __init__(self, color, name, is_police, speed):
        self.color = color
        self.name = name
        self.is_police = is_police
        self.speed = speed

    def go(self):
        print(f'Авто {self.name} поехала')

    def stop(self):
        print(f'Авто {self.name} остановилась')

    def turn(self, direction):
        print(f'Авто {self.name} повернуло на {direction}')

    def show_speed(self):
        print(f'Авто {self.name} движется со скоростью {self.speed} км/ч')


class TownCar(Car):
       def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Авто {self.name} превысило макс. скорость {60} км/ч')



class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Авто {self.name} превысило макс. скорость {40} км/ч')


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, color, name, is_police, speed):
        super().__init__(color, name, True, speed)


town_car = TownCar("Черная", "Volvo", False, 70)
town_car.go()
TownCar.show_speed(town_car)
print()
work_car = WorkCar("Серая", "Lada", False, 40)
work_car.turn("Налево")
work_car.show_speed()
print()
town_car = PoliceCar("Бело-синяя", "Shkoda", True, 100)
town_car.go()
town_car.show_speed()

# PoliceCar
