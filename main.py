# Модуль 8-5 классы
# Кошлаков Евгений Python 320-2
# Множественное наследование, реализация магических методов.

# Задача 1
# Создать базовый класс Фигура с методом для подсчета площади. Создать производные классы: прямоугольник, круг,
# прямоугольный треугольник, трапеция со своими методами для подсчета площади.
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self, radius):
        return 3.14 * radius ** 2


class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class Triangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


class Trapezoid(Figure):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def calculate_area(self):
        return 0.5 * (self.base1 + self.base2) * self.height


circle = Circle(5)
rectangle = Rectangle(5, 10)
triangle = Triangle(5, 10)
trapezoid = Trapezoid(5, 10, 5)

print(circle.calculate_area(5))
print(rectangle.calculate_area())
print(triangle.calculate_area())
print(trapezoid.calculate_area())


# Задача 2
# Для классов из задачи 1 нужно переопределить магические методы int(возвращает площадь) и str(возвращает информацию о
# фигуре).


class Figure(ABC):
    @abstractmethod
    def calculate_area(self, area):
        pass

    @abstractmethod
    def __int__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def __int__(self):
        return int(self.calculate_area(self.radius))

    def __str__(self):
        return f'Круг с радиусом {self.radius}'

    def calculate_area(self, radius):
        return 3.14 * radius ** 2


class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __int__(self):
        return int(self.calculate_area())

    def __str__(self):
        return f'Прямоугольник с длиной {self.length} и шириной {self.width}'

    def calculate_area(self):
        return self.length * self.width


class Triangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def __int__(self):
        return int(self.calculate_area())

    def __str__(self):
        return f'Треугольник с основанием {self.base} и высотой {self.height}'

    def calculate_area(self):
        return 0.5 * self.base * self.height


class Trapezoid(Figure):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def __int__(self):
        return int(self.calculate_area())

    def __str__(self):
        return f'Трапеция с основаниями {self.base1}, {self.base2} и высотой {self.height}'

    def calculate_area(self):
        return 0.5 * (self.base1 + self.base2) * self.height


circle = Circle(5)
rectangle = Rectangle(5, 10)
triangle = Triangle(5, 10)
trapezoid = Trapezoid(5, 10, 5)

print(int(circle))
print(str(circle))
print(int(rectangle))
print(str(rectangle))
print(int(triangle))
print(str(triangle))
print(int(trapezoid))
print(str(trapezoid))
