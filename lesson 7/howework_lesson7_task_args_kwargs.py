# Напишите функцию make_sentence, которая принимает один именованный
# аргумент words, который должен быть списком строк, и возвращает строку,
# составленную из элементов списка, разделенных пробелами и
# заканчивающуюся точкой. Если аргумент words не указан, то по умолчанию
# используется список ["This", "is", "a", "sentence"].
from typing import Any


def make_sentence(words: list[str] = ["This", "is", "a", "sentence"]) -> str:
    return " ".join(words) + "."


print(make_sentence(words=["Python", "is", "fun", "language"]))


# Напишите функцию sum_of_squares, которая принимает произвольное
# количество позиционных аргументов, которые должны быть числами, и
# возвращает сумму их квадратов. Если функции не передано ни одного
# аргумента, она должна вернуть 0.

def sum_of_squares(*numbers: int) -> int:
    return sum(map(lambda x: x ** 2, numbers))

print("Sosi")
print(sum_of_squares())


# Напишите функцию greet, которая принимает два именованных аргумента:
# name и language. Аргумент name должен быть строкой, а аргумент language
# должен быть одним из трех возможных значений: "en", "ru" или "fr".
# Функция должна возвращать приветствие на выбранном языке.
# Если аргумент language не указан, то по умолчанию используется "en".
# Пример вызова:
# greet(name="Anna", langua\

def greet(name: str, language: str = "en") -> str:
    language_privet = {
        "en": "English",
        "ru": "Привет",
        "fr": "Bonjour"
    }
    return f"{language_privet.get(language, "Unknown language")}, {name}!"


print(greet(name="Anna", language="fr"))


# Напишите функцию print_info, которая принимает произвольное
# количество именованных аргументов (**kwargs) и выводит их в формате
# "key: value" по одной паре на строку. Напоминаю, что kwargs в функции
# будет словарем. Если функции не передано ни одного аргумента, она должна
# вывести "No info given.".

def print_info(**kwargs: dict[str, Any]) -> None:
    print("No info given." if not kwargs else '', end='')
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info()
print()


# Напишите функцию print_table, которая принимает произвольное
# количество именованных аргументов в виде пар ключ-значение и выводит их
# в виде таблицы с двумя столбцами: "Key" и "Value". Если функции не
# передано ни одного аргумента, она должна вывести "No data given.".
def print_table(**kwargs: dict[str, Any]) -> None:
    print("No info given." if not kwargs else '', end='')
    max_len_key = max(map(lambda x: len(str(x)), kwargs.keys()))
    max_len_value = max(map(lambda x: len(str(x)), kwargs.values()))
    print(f"| Key: {" " * (max_len_key - 4)} | Value: {(max_len_value - 6) * " "} |")
    for key, value in kwargs.items():
        print(f"| {key} {" " * (max_len_key - len(str(key)))} | {value} {" " * (max_len_value - len(str(value)))} |")


print_table(name="Bob", age=30, city="Amsterdam", second_name="Veremchuk", nikname="LASFASFASFaSFasf")


# Напишите функцию calculate, которая принимает произвольное количество
# позиционных аргументов, которые должны быть числами, и один
# именованный аргумент operation, который должен быть одним из четырех
# возможных значений: "+", "-", "*" или "/".
# Функция должна возвращать результат выполнения указанной операции над
# всеми числами в порядке их передачи.
# Если функции не передано ни одного позиционного аргумента, она должна
# вернуть 0.
# Если аргумент operation не указан, то по умолчанию используется "+".
# Пример вызова: calculate(1, 2, 3, operation="*")

def calculate(*args: int | float, operation: str = "+") -> int | float:
    if operation == "+":
        res = sum(args)
    elif operation == "-":
        res = args[0]
        for arg in args[1:]:
            res -= arg
    elif operation == "*":
        res = args[0]
        for arg in args[1:]:
            res *= arg
    elif operation == "/":
        res = args[0]
        for arg in args[1:]:
            res /= arg
    return 0 if res == 0 else res


print(calculate(1, 2, 3, 4, operation="*"))


# Напишите функцию print_triangle, которая принимает один именованный
# аргумент height, который должен быть положительным целым числом, и
# выводит равнобедренный треугольник из символов "*" с заданной высотой.
# Если аргумент height не указан, то по умолчанию используется число 5.
# Пример вызова: print_triangle(height=4)

def print_triangle(height: int = 5) -> None:
    for i in range(1, height + 1):
        print(f"{(height - i) * " "}{(2 * i - 1) * "*"}")


print_triangle()


# Напишите функцию create_post, которая создает пост для блога,
# основываясь на переданных параметрах. Обязательными параметрами
# являются: заголовок, содержимое и автор. Необязательным параметром
# является категория. Если она не была передана, то по умолчанию будет
# текущая значение “general”. Функция должна возвращать словарь поста.

def create_post(heading: str, content: str, name_of_author: str, categories: str = "general") -> dict[str, str]:
    return {"heading": heading, "content": content, "name_of_author": name_of_author, "categories": categories}


# Напишите функцию create_product, которая создает товар для интернет
# магазина, основываясь на переданных параметрах. Обязательными
# параметрами являются: имя, цена и категория. Необязательным параметром
# является рейтинг. Если он не был передан параметр, то по умолчанию будет
# 0. Функция должна возвращать словарь товара.

def create_product(name_of_product: str, price: int, categories: str, rating: int = 0) -> dict[str, str | int]:
    return {"name": name_of_product, "price": price, "categories": categories, "rating": rating}


#  Напишите функцию create_student, которая создает словарь студента
# для учебного заведения, основываясь на переданных параметрах.
# Обязательными параметрами являются: имя, фамилия, отчество и группа.
# Также дополнительными параметрами могут быть: дата поступления в виде
# строки «19.10.2023», средний бал, семестр обучения, номер телефона, адрес.
# Функция должна возвращать словарь студента только с переданными
# данными, если некоторые данные не были переданы, то их не должно быть
# в словаре.

def create_student(name: str, surname: str, patronymic: str, group: int, **kwargs) -> dict[str, str]:
    return {"name": name, "surname": surname, "patronymic": patronymic, "group": group, **kwargs}


student2 = create_student(
    "Анна", "Сидорова", "Сергеевна", "БИ-102",
    enrollment_date="19.10.2023",
    average_grade=4.8,
    phone="+7-999-123-45-67"
)
print("Студент 2 (с дополнительными параметрами):")
print(student2)
