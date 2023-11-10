# Создать класс Country: Столица, Площадь, Численность населения.
# Создать список объектов. Вывести:
# a) список стран по заданной площади;
# b) список стран по заданной численности населения. –

class Country:
    city = ""
    square = 0
    population = 0

    def __init__(self, city, square, population):
        self.city = city
        self.square = square
        self.population = population


countries = [
    Country("Минск", 207_600, 9_340_000),
    Country("Москва", 17_100_000, 143_400_000),
    Country("Киев", 603_628, 43_790_000),
    Country("Варшава", 322_575, 37_750_000),
]
min_square = 400_000
min_population = 40_000_000
for country in countries:
    if country.square >=min_square:
        print(f'Столица: г.{country.city}  Площадь: {country.square} км^2')

print("")
for country in countries:
    if country.population >=min_population:
        print(f'Столица: г.{country.city}  Численность: {country.population} чел.')