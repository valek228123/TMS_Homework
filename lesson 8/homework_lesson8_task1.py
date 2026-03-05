# Напишите код, который принимает список чисел и возвращает новый список,
# содержащий только четные числа из исходного списка. Используйте функцию
# filter и лямбда-выражение.


def only_even(list: list) -> list:
    return [item for item in list if item % 2 == 0]


print(only_even([1, 2, 3, 4, 5]))
print(only_even([]))


# Напишите код, который принимает список кортежей вида (имя, возраст) и
# возвращает новый список, отсортированный по возрастанию возраста.
# Используйте функцию sorted и ключ сортировки.

def sorted_by_age(list1: list[tuple[str | int, ...]]) -> list:
    return sorted(list1, key=lambda x: x[1])


print(sorted_by_age([("Виталик", 78), ("Валентин", 4), ("Валентин", 11)]))


# апишите код, который принимает список строк и возвращает новый список,
# содержащий только те строки, которые начинаются с гласной буквы. (Да да,
# снова эти гласные) Используйте функцию filter и множество.

def list_vowel(list_of_strings: list[str]) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return list(filter(lambda x: x[0].lower() in vowels, list_of_strings))


# Напишите код, который принимает список чисел и возвращает новый список,
# содержащий квадраты этих чисел. Используйте функцию map и lambda.

def build_into_to_square(list_of_numbers: list[int]) -> list[int]:
    return list(map(lambda x: x ** 2, list_of_numbers))


print(build_into_to_square([1, 2, 3, 4, 5]))


# Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по убыванию длины слов. Используйте функцию sorted и
# обратный порядок сортировки.

def change_list_by_len(list_of_words: list[str]) -> list[str]:
    return sorted(list_of_words, reverse=True, key=len)


print(change_list_by_len(["umbrella", "aqnt", "oak", "banaqna"]))


# Напишите код, который принимает строку и возвращает список, содержащий
# только те буквы, которые встречаются в слове “python”. Используйте функцию
# filter и оператор in.


def change_only_with_python(list_of_words: list[str]) -> list[str]:
    return list(filter(lambda x: x.lower() in "python", list_of_words))


# Напишите код, который принимает список чисел и возвращает новый список,
# содержащий эти же числа, умноженные на 10. Используйте функцию.

def change_list(list_of_numbers: list[int]) -> list[int]:
    return [i * 10 for i in list_of_numbers]


print(change_list([1, 2, 3, 4, 5, 6, 7, 8]))


# Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по алфавиту. Используйте функцию sorted.

def sort_list(list_of_words: list[str]) -> list[str]:
    return sorted(list_of_words)


print(sort_list(["bsdasd", "afbdsbsdfb", "cascasc<kasdlkwak", "oqjweijoqr", "dsdasdqwd", "lqpwelqwlpe"]))


# Напишите функцию, которая принимает список строк и возвращает новый
# список, содержащий только те строки, которые являются палиндромами.
# Палиндром — это слово, которое читается одинаково слева направо и справа
# налево. Используйте функцию filter и сравнение строк.

def sort_list(list_of_words: list[str]) -> list[str]:
    return list(filter(lambda x: x == x[::-1], list_of_words))


print(sort_list(["abccba", "rfrfirb", "топот", "kakashka"]))


# Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по возрастанию количества гласных букв в словах.
# Используйте функцию sorted и ключ сортировки.


def sort_list(list_of_words: list[str]) -> list[str]:
    vowels = 'aeiou'
    return sorted(list_of_words, key=lambda word: sum(1 for ch in word if ch.lower() in vowels))


print(sort_list(["abccba", "rfrfirb", "cascasc<kasdlkwak", "kakashka"]))


#  Напишите код, который принимает список строк и возвращает новый список,
# содержащий эти же строки в верхнем регистре. Используйте функцию map и
# встроенный метод строк upper.

def change_list(list_of_numbers: list[str]) -> list[str]:
    return list(map(lambda x: x.upper(), list_of_numbers))


print(change_list(["abccba", "rfrfirb", "топот", "kakashka"]))


# Напишите код, который принимает список строк и возвращает новый список,
# содержащий эти же строки с добавленным префиксом “Hello”. Используйте
# функцию map и конкатенацию строк.

def change_list(list_of_numbers: list[str]) -> list[str]:
    return list(map(lambda x: x + "Hello", list_of_numbers))


print(change_list(["abccba", "rfrfirb", "топот", "kakashka"]))


# Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по возрастанию количества букв “a” в словах. Используйте
# функцию sorted и ключ сортировки.

def sort_list(list_of_numbers: list[str]) -> list[str]:
    return sorted(list_of_numbers, key=lambda words: sum(1 for i in words if i == "a"))


print(sort_list(["abaa", "acwe", "asa", "kakashkaa"]))


# Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по возрастанию количества уникальных букв в словах.
# Используйте функцию sorted и ключ сортировки.

def sort_list(list_of_numbers: list[str]) -> list[str]:
    return sorted(list_of_numbers, key=lambda words: len(set(words)))


print(sort_list(["abc", "abcd", "a", "ab"]))


# Напишите декоратор retry_five, который повторяет вызов декорируемой
# функции 5 раз.

def retry_five(func):
    def wrapper(*args, **kwargs):
        for i in range(5):
            func(*args, **kwargs)

    return wrapper


@retry_five
def print_power_of_two(num: int):
    print(2 ** num)


print_power_of_two(5)
