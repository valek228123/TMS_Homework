# Task 1
# Создайте класс Soda (для определения типа газированной воды), принимающий
# 1 аргумент при инициализации (отвечающий за добавку к выбираемому
# лимонаду). В этом классе реализуйте метод show_my_drink(), выводящий на
# печать «Газировка и {ДОБАВКА}» в случае наличия добавки, а иначе
# отобразится следующая фраза: «Обычная газировка».
class Soda():
    def __init__(self, supplement: str = None):
        self.supplement = supplement

    def show_my_drink(self):
        if taste is None:
            print("У вас обычная газировка")
        else:
            print(f"Газировка и {self.supplement}")


# Task 2
# Требуется проверить, возможно ли из представленных отрезков условной длины
# сформировать треугольник. Для этого необходимо создать класс
# TriangleChecker, принимающий только положительные числа. С помощью
# метода is_triangle() возвращаются следующие значения (в зависимости от
# ситуации):
# – Ура, можно построить треугольник!;
# – С отрицательными числами ничего не выйдет!;
# – Нужно вводить только числа!;
# – Жаль, но из этого треугольник не сделать.
class TriangleChecker():
    def __init__(self, side1: int, side2: int, side3: int):
        # if side1 <= 0 or side2 <= 0 or side3 <= 0:
        #     raise ValueError("Сторонны могут быть только положительными")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def is_triangle(self):
        if isinstance(self.side1, int) and isinstance(self.side2, int) and isinstance(self.side3, int):
            if self.side1 <= 0 or self.side2 <= 0 or self.side3 <= 0:
                return "Сторонны могут быть только положительными"
            elif self.side1 + self.side2 > self.side3 and self.side2 + self.side3 > self.side1 and self.side1 + self.side3 > self.side2:
                return "Ура, можно построить треугольник!"
            else:
                return "Жаль, но из этого треугольник не сделать."

        else:
            return "Нужно вводить только числа!"


# Task 3
# Необходимо создать класс KgToPounds, в который принимает количество
# килограмм, а с помощью метода to_pounds() они переводятся в фунты.
# Необходимо закрыть доступ к переменной kg.
# Также, реализовать методы: - set_kg() - для задания нового значения килограммов (записывать только
# числовые значения),  - get_kg() - для вывода текущего значения кг.
# Во второй версии необходимо использовать декоратор property для создания
# setter и getter взамен set_kg и get_kg.
class KgToPounds():
    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2, 2

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, kg):
        if kg <= 0 or isinstance(kg, int) or isinstance(kg, float):
            raise ValueError("Введите корректные данные")
        self.__kg = kg


# Task 4
# Cтроки в Питоне сравниваются на основании значений символов. Т.е. если мы
# захотим выяснить, что больше: Apple или Яблоко, – то Яблоко окажется
# бОльшим. А все потому, что английская буква A имеет значение 65 (берется из
# таблицы кодировки), а русская буква Я – 1071. Надо создать новый класс
# RealString, который будет принимать строку и сравнивать по количеству
# входящих в них символов. Сравнивать между собой можно как объекты класса,
# так и обычные строки с экземплярами класса RealString

class RealString():
    def __init__(self, real_string):
        if isinstance(real_string, str):
            self.real_string = real_string
        else:
            raise ValueError("Должна быть строка")

    def __eq__(self, other):
        if isinstance(other, RealString):
            return len(self.real_string) == len(other.real_string)
        elif isinstance(other, str):
            return len(self.real_string) == len(other)
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, RealString):
            return len(self.real_string) != len(other.real_string)
        elif isinstance(other, str):
            return len(self.real_string) != len(other)
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, RealString):
            return len(self.real_string) < len(other.real_string)
        elif isinstance(other, str):
            return len(self.real_string) < len(other)
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, RealString):
            return len(self.real_string) > len(other.real_string)
        elif isinstance(other, str):
            return len(self.real_string) > len(other)
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, RealString):
            return len(self.real_string) <= len(other.real_string)
        elif isinstance(other, str):
            return len(self.real_string) <= len(other)
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, RealString):
            return len(self.real_string) >= len(other.real_string)
        elif isinstance(other, str):
            return len(self.real_string) >= len(other)
        else:
            return NotImplemented


# Task 5
# Напишите класс Rectangle, который имеет атрибуты: width (ширина) и
# height (высота). Класс должен иметь следующие методы:
# • Конструктор, который принимает два параметра: width и height, и
# инициализирует соответствующие атрибуты.
# • Метод str, который возвращает строковое представление объекта класса
# Rectangle в формате “Прямоугольник с шириной width и высотой
# height”.
# • Метод get_area, который возвращает площадь прямоугольника.
# • Метод get_perimeter, который возвращает периметр прямоугольника.
# • Метод is_square, который возвращает True, если прямоугольник является
# квадратом, и False в противном случае. Этот метод должен быть
# декорирован как property.


class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Прямоугольник с шириной {self.width} и высотой {self.height}"

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    @property
    def is_square(self):
        return self.width == self.height


# Task 6.
# Напишите класс Person, который имеет атрибуты name (имя), age (возраст)
# и gender (пол). Класс должен иметь следующие методы:
# • Конструктор, который принимает три параметра: name, age и gender, и
# инициализирует соответствующие атрибуты.
# • Метод str, который возвращает строковое представление объекта класса
# Person в формате “Имя: name, Возраст: age, Пол: gender”.
# • Метод get_name, который возвращает значение атрибута name.
# • Метод set_name, который принимает один параметр: new_name, и
# устанавливает значение атрибута name равным new_name. Этот метод
# должен быть декорирован как property.
# • Метод is_adult, который возвращает True, если возраст объекта больше
# или равен 18, и False в противном случае. Этот метод должен быть
# декорирован как staticmethod.
# • Метод create_from_string, который принимает один параметр: s, и
# создает и возвращает объект класса Person на основе строки s. Строка s
# должна иметь формат “name-age-gender”, где name - имя, age - возраст и
# gender - пол. Этот метод должен быть декорирован как classmethod.


class Person():
    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    def __str__(self):
        return f"Имя: {self._name}, Возраст: {self._age}, Пол: {self._gender}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @staticmethod
    def is_abult(age):
        return age >= 18


    @classmethod
    def create_from_string(cls, s):
        list_s = s.split("-")
        return cls(list_s[0], int(list_s[1]), list_s[2])


a = Person("Иван", 64, "Мужской")
b = Person.create_from_string("Илья-52-Женский")
print(b)
