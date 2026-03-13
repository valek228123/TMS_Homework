# Task 1
import time


class Auto():
    def __init__(self, brand: str, age: int, mark: str, color: str = None, weight: float = None) -> None:
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print("Move")

    def stop(self):
        print("Stop")

    def bithday(self):
        self.age += 1


# Task 2

class Truck(Auto):
    def __init__(self, brand: str,
                 age: int,
                 mark: str,
                 max_load: int,
                 color: str = None,
                 weight: float = None,
                 ):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print("Attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand: str,
                 age: int,
                 mark: str,
                 max_speed: int,
                 color: str = None,
                 weight: float = None,
                 ):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max speed if {self.max_speed}")


truck1 = Truck("Volvo", 5, "FH16", 20000, "red", 8000)
truck2 = Truck("Scania", 3, "R500", 15000, "blue", 7500)

car1 = Car("Toyota", 2, "Camry", 180, "black", 1500)
car2 = Car("BMW", 4, "X5", 220, "white", 2000)

truck1.move()
truck2.load()
truck1.bithday()
print(truck1.age)
car1.move()
car2.stop()

# Task 3

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Point():
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __add__(self, other):
        return self.radius + other.radius

    def __sub__(self, other):
        return Point() if self.radius == other.radius else self.radius - other.radius


circle1 = Circle(4)
circle2 = Circle(2)
print(circle1 + circle2)
print(circle1 - circle2)
