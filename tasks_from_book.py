# Задание 1
# Определите функцию filter_strings_containing_a, принимающую
# один параметр:
# Имя
# input_strs
# Тип
# список строк
# Пример	входа
# ["apple", "banana", "cherry", "date"]
# Функция должна возвращать новый список, содержащий только
# строки, содержащие букву «a»

def filter_string_containing_a(input_strs: list[str]) -> list[str]:
    new_strings = list()
    for input_str in input_strs:
        if "a" in input_str:
            new_strings.append(input_str)
    return new_strings


print(filter_string_containing_a(["apple", "banana", "cherry", "date"]))


# Задание 2
# Определите функцию sum_if_less_than_fifty, принимающую два па
# раметра:
# Имя
# num_one
# num_two
# Тип
# int
# Пример	входа
# 20
# Int
# 25
# Функция должна возвращать:
# сумму двух чисел, если эта сумма меньше 50;
# None, если сумма двух чисел больше или равна 50

def sum_if_less_than_fifty(num_one: int, num_two: int) -> int:
    return num_one + num_two if num_one + num_two < 50 else None


print(sum_if_less_than_fifty(20, 20))
print(sum_if_less_than_fifty(20, 30))


# Задача 3
# Определите функцию sum_even, принимающую один параметр:
# Имя
# input_nums
# Тип
# Пример	входа
# список int
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Функция должна возвращать сумму всех четных чисел в списке:

def sum_even(input_nums: list[int]) -> int:
    list_even = list()
    for num in input_nums:
        if num % 2 == 0:
            list_even.append(num)
    return sum(list_even)


print(sum_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(sum_even([10, 20, 30, 40, 50]))
print(sum_even([9, 7, 5, 3, 1]))

# Задание 4
# Определите функцию remove_vowels, принимающую один пара
# метр:
# Имя
# input_str
# Тип
# Пример	входа
# str
# «Hello, World!»
# Функция должна возвращать новую строку, из которой удалены
# все гласные.

vowel_letters = ['a', 'e', 'i', 'o', 'u', 'y']


def remove_vowels(input_str: str) -> str:
    new_string = ''
    for letter in input_str.lower():
        if letter not in vowel_letters:
            new_string += letter
    return new_string


print(remove_vowels("Hello, World!"))
print(remove_vowels("aeiouAEIOU"))
print(remove_vowels("zzxxxccvvvbbnnmmmLLKKJJHH"))


# Задача 6
# Задание
# Определите функцию filter_even_length_strings, принимающую один
# параметр:
# Имя
# input_strs
# Тип
# Пример	входа
# список строк [«cat», «dog», «fish», «elephant»]
# Функция должна возвращать новый список, в котором оставле
# ны только строки, содержащие четное число символов

def filter_even_length_strings(input_strs: list[str]) -> list[str]:
    new_strings = list()
    for input_str in input_strs:
        if len(input_str) % 2 == 0:
            new_strings.append(input_str)
    return new_strings


print(filter_even_length_strings(["cat", "dog", "fish", "elephant"]))
print(filter_even_length_strings(["q", "w", "e", "r", "t", "y"]))
print(filter_even_length_strings(["qq", "ww", "ee", "rr", "t", "yy"]))


# Определите функцию reverse_elements, принимающую один пара
# метр:
# Имя
# input_nums
# Тип
# Пример	входа
# список int
# [1, 2, 3, 4, 5]
# Функция должна возвращать новый список, в котором порядок
# элементов исходного списка изменен на противоположный.

def reverse_elements(input_nums: list[int]) -> list[int]:
    return input_nums.copy()[::-1]


print(reverse_elements([1, 2, 3, 4, 5]))
print(reverse_elements([]))
print(reverse_elements([20, 15, 25, 10, 30, 5, 0]))


# Задача 8
# Задание
# Определите функцию filter_type_str, принимающую один параметр:
# Имя Тип Пример	входа
# input_list список строк или int
# [«hello”, 1, 2, “www”]
# Функция должна возвращать новый список, содержащий только
# строки из оригинального списка
def filter_type_str(input_list: list[str | int]) -> list[str]:
    new_list = list()
    for item in input_list:
        if isinstance(item, str):
            new_list.append(item)
    return new_list


print(filter_type_str(["hello", 1, 2, "www"]))
print(filter_type_str([]))
print(filter_type_str([1, 2, 3, 4, 5]))


# Задача 9
# Определите функцию string_to_morse_code, принимающую один па
# раметр:
# Имя Тип Пример	входа
# input_str str
# «HELLO, WORLD!»
# Функция должна возвращать код Морзе, эквивалентный входной
# строке. Функция должна удовлетворять следующим требованиям:
# код Морзе «точка» должен быть представлен точкой;
# код Морзе «тире» должен быть представлен дефисом;
# между любыми двумя буквами в коде Морзе должен быть
# пробел, например «.-(пробел)-...»;
# функция должна поддерживать следующие символы во вход
# ной строке:– цифры и буквы, строчные и заглавные;– специальные символы (, . : ? ‘ - / ( ) “ @ = + !);
# если во входной строке встречается пробел, то в выходной он
# должен быть представлен косой чертой

def string_to_morse_code(input_str: str) -> str:
    morse_dict = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..",
                  "e": ".", "f": "..-.", "g": "--.", "h": "....",
                  "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
                  "m": "--", "n": "-.", "o": "---", "p": ".--.",
                  "q": "--.-", "r": ".-.", "s": "...", "t": "-",
                  "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                  "y": "-.--", "z": "--..", "0": "-----", "1": ".----",
                  "2": "..---", "3": "...--", "4": "....-", "5": ".....",
                  "6": "-....", "7": "--...", "8": "---..", "9": "----.",
                  ",": "--..--", ".": ".-.-.-", ":": "---...", "?": "..--..",
                  "'": ".----.", "-": "-....-", "/": "-..-.", "(": "-.--.",
                  ")": "-.--.-", '"': ".-..-.", "@": ".--.-.", "=": "-...-",
                  "+": ".-.-.", "!": "-.-.--"}
    morse_code = ""
    for letter in input_str.lower():
        morse_code += morse_dict[letter] if letter != " " else " "
    return morse_code


print(string_to_morse_code("HELLO, WORLD!"))
print(string_to_morse_code("abcdefghijklmnopqrstuvwxyz,.:?'-/()\"@=+!"))
print(string_to_morse_code(""))


# Задание 10
# Определите функцию get_second_largest_number, принимающую
# один параметр:
# Имя Тип Пример	входа
# input_nums список int
# [1, 2, 3, 4, 5]
# Функция должна возвращать второе по величине число в списке.
# Если второго по величине числа нет, то функция должна возвра
# щать None.

def get_second_largest_number(input_nums: list[int]) -> int | None:
    numbers_set = set(input_nums)
    numbers_set.remove(max(numbers_set))
    if numbers_set:
        return max(numbers_set)
    else:
        return None


print(get_second_largest_number([1, 2, 3, 4, 5]))
print(get_second_largest_number([3, 45, 345, 435, 345, 43, 56, 34, 234, 34]))
print(get_second_largest_number([1]))


# Задача 11
# Определите функцию format_number_with_commas, принимающую
# один параметр:
# Имя Тип Пример	входа
# input_num int
# 1000000
# Функция должна возвращать строковое представление числа,
# в котором группы по 3 разряда (начиная справа) разделены за
# пятыми.

def format_number_with_commas_difficult(input_num: int) -> str:
    is_negative = input_num < 0
    numbers_of_coma = (len(str(input_num)) - 1) // 3
    list_input_num = list(str(input_num)[::-1])
    index = 3
    for i in range(numbers_of_coma):
        list_input_num.insert(index, ",")
        index += 4
    result = ("".join(list_input_num))[::-1]
    return "-" + result if is_negative else result


def format_number_with_commas_easy(input_nums: list[int]) -> str:
    return f"{input_nums:,}"


print(format_number_with_commas_difficult(100))
print(format_number_with_commas_difficult(1000000))
print(format_number_with_commas_easy(1000000))
print(format_number_with_commas_easy(12345))
print(format_number_with_commas_easy(-99999999))
print(format_number_with_commas_easy(1234567890))
print(format_number_with_commas_easy(1000))
print(format_number_with_commas_easy(0))
print(format_number_with_commas_easy(-42))


# Задача 12
# Определите функцию string_to_ascii, принимающую один пара
# метр:
# Имя Тип Пример	входа
# input_str str
# «Programming puzzles!»
# Функция должна возвращать список, содержащий числовые
# ASCII-коды всех символов строки.


def string_to_ascii(input_str: str) -> list[int]:
    return [ord(i) for i in input_str]


print(string_to_ascii("Programming puzzles!"))
print(string_to_ascii(""))
print(string_to_ascii("aA"))


# Задача 12.1
# Определите функцию ascii_to_string, принимающую один пара
# метр:
# Имя
# Тип
# Пример	входа
# input_ascii_codes список int [80, 114, 111, 103, 114, 97, 109, 109, 105, 110,
# 103, 32, 112, 117, 122, 122, 108, 101, 115, 33]
# Функция должна возвращать строку, содержащую символы
# с указанными в списке ASCII-кодами

def ascii_to_string(input_ascii_codes: list[int]) -> str:
    return "".join([chr(i) for i in input_ascii_codes])


print(ascii_to_string([80, 114, 111, 103, 114, 97, 109, 109, 105,
                       110, 103, 32, 112, 117, 122, 122, 108, 101, 115, 33]))
print(ascii_to_string([]))
print(ascii_to_string([97, 65]))


# Задача 13
# Определите функцию filter_strings_with_vowels, принимающую один
# параметр:
# Имя Тип Пример	входа
# input_strs список str
# ["apple", "banana", "zyxvb"]
# Функция должна возвращать новый список, содержащий строки,
# в которых есть хотя бы одна гласная.

def filter_strings_with_vowels(input_strs: list[str]) -> list[str]:
    vowels = ["a", "e", "i", "o", "u"]
    list1 = []
    for world in input_strs:
        for letter in world:
            if letter.lower() in vowels:
                list1.append(world)
                break
    return list1


print(filter_strings_with_vowels(["apple", "banana", "zyxvb"]))
print(filter_strings_with_vowels([]))
print(filter_strings_with_vowels(["q", "w", "e", "r", "t", "y"]))


# Задача 14
# Определите функцию reverse_first_five_positions, принимающую
# один параметр:
# Имя Тип Пример	входа Ограничение
# input_nums список int [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# len(input_nums) == 10
# Функция должна возвращать новый список, в котором первые
# пять элементов оригинального списка переставлены в обратном
# порядке. В решении следует использовать срезы Python и не ис
# пользовать циклы.

def reverse_first_five_positions(input_nums: list[int]) -> list[int]:
    new_list = input_nums[:5][::-1]
    new_list.extend(input_nums[5:])
    return new_list


print(reverse_first_five_positions([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(reverse_first_five_positions([100, 90, 80, 70, 60, 50, 40, 30, 20, 10]))
print(reverse_first_five_positions([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]))


#  Задача 15
#  Определите функцию filter_palindromes, принимающую один па
# раметр:
# Имя
# input_strs
# Тип
# Пример	входа
# список str
# ["cat", "dog", "racecar", "deified", "giraffe"]
# Функция должна возвращать новый список, содержащий только
# строки, являющиеся палиндромами.

def filter_palindromes(input_strs: list[str]) -> list[str]:
    return list(filter(lambda word: word == word[::-1], input_strs))


print(filter_palindromes(["cat", "dog", "racecar", "deified", "giraffe"]))
print(filter_palindromes(["kayak", "deified", "rotator", "repaper", "deed",
                          "a"]))
print(filter_palindromes(["ab", "ba", "cd", "ef", "pt"]))


# Задача 16
# Задание
# Определите функцию censor_python, принимающую один пара
# метр:
# Имя Тип
# input_strs список str
# Пример	входа
# ["python", "hello", "HELLO"]
# Функция должна возвращать новый список строк, в которых
# буквы «P», «Y», «T», «H», «O», «N» (в любом регистре) заменены
# буквой «X».


def censor_python(input_strs: list[str]) -> list[str]:
    list_python = ["p", "y", "t", "h", "o", "n"]
    new_list = []
    for word in input_strs:
        temporary_list = []
        for letter in word:
            if letter.lower() in list_python:
                temporary_list.append("X")
            else:
                temporary_list.append(letter)
        new_list.append("".join(temporary_list))
    return new_list


print(censor_python(["python", "hello", "HELLO"]))
print(censor_python(["abcdefg"]))
print(censor_python([]))


# Задача 17
# Определите функцию check_if_string_is_happy, принимающую один
# параметр:
# Имя Тип
# input_str str
# Пример	входа
# "abcdefg"
# Функция должна возвращать булево значение, показывающее,
# является строка счастливой или нет.

def check_if_string_is_happy(input_str: str) -> bool:
    for i in range(2, len(input_str)):
        if (input_str[i] != input_str[i - 1] and
                input_str[i - 1] != input_str[i - 2] and
                input_str[i] != input_str[i - 2]):
            continue
        else:
            return False
    return True


# Задание 18
# Определите функцию get_number_of_digits, принимающую один па
# раметр:
# Имя Тип Пример	входа Ограничение
# input_num int 1234
# input_num >= 0
# Функция должна возвращать количество цифр в input_num.
# Дополнительные условия:
# функция должна быть рекурсивной;
# функция не должна преобразовывать целое в строку

def get_number_of_digits(input_num: int, index: int = 0) -> int:
    if index == 0 and input_num == 0:
        return 1
    if input_num == 0:
        return index
    return get_number_of_digits(input_num // 10, index + 1)


print(get_number_of_digits(1234))
print(get_number_of_digits(0))
print(get_number_of_digits(1))
print(get_number_of_digits(11))
print(get_number_of_digits(123456789))
print()


# Определите функцию get_tic_tac_toe_winner, принимающую один параметр:
# Имя Тип
# input_board список списков строк
# Пример	входа
# [["X", "X", "X"], ["O", "X", "O"],
# ["X", "O", "O"]]
# Функция должна определять, кто выиграл. В случае ничьей она  должна вернуть None
def get_tic_tac_toe_winner(input_board: list[list[str]]) -> str | None:
    for row in input_board:
        winning_combinations_row = []
        for col in row:
            winning_combinations_row.append(col)
        if winning_combinations_row == ["X", "X", "X"]:
            return "X"
        elif winning_combinations_row == ["O", "O", "O"]:
            return "O"
    for col in range(len(input_board)):
        winning_combinations_col = []
        for row in range(len(input_board[0])):
            winning_combinations_col.append(input_board[row][col])
        if winning_combinations_col == ["X", "X", "X"]:
            return "X"
        elif winning_combinations_col == ["O", "O", "O"]:
            return "O"
    winning_combinations_diagonal1 = []
    for row in range(len(input_board)):
        winning_combinations_diagonal1.append(input_board[row][row])
    if winning_combinations_diagonal1 == ["X", "X", "X"]:
        return "X"
    elif winning_combinations_diagonal1 == ["O", "O", "O"]:
        return "O"
    winning_combinations_diagonal2 = []
    for row in range(len(input_board)):
        winning_combinations_diagonal2.append(input_board[row][len(input_board[0]) - row - 1])
    if winning_combinations_diagonal2 == ["X", "X", "X"]:
        return "X"
    elif winning_combinations_diagonal2 == ["O", "O", "O"]:
        return "O"


print(get_tic_tac_toe_winner([["X", "X", "X"], ["O", "X", "O"], ["X", "O", "O"]]))
print(get_tic_tac_toe_winner([["X", "O", "O"], ["O", "O", ""], ["X", "O", "O"]]))
print(get_tic_tac_toe_winner([["X", "O", "O"], ["O", "X", ""], ["X", "O", "O"]]))


# Задача 20
# Задание
# Определите функцию print_triangle, принимающую два параметра:
# Имя
# number_of_levels
# symbol
# Тип
# int
# Пример	входа
# 4
# str
# "*"
# Функция должна вывести симметричный относительно верти
# кальной оси треугольник, составленный из указанных символов.
# Количество символов в каждой строке должно увеличиваться на
# два при переходе к следующему уровню: на первом уровне должен
# быть один символ, на втором – три и т. д., пока не будет выведен
# конечный уровень. Например, при number_of_levels = 4 и symbol =
# "*" должен получиться такой треугольник:
def print_triangle(number_of_levels: int, symbol: str) -> None:
    if number_of_levels != 1:
        sum_of_symbols = 1
        for i in range(number_of_levels):
            print((symbol * sum_of_symbols).center(number_of_levels + 2))
            sum_of_symbols += 2
    else:
        print(symbol)


print_triangle(6, "*")
print_triangle(1, "|")
print_triangle(0, "|")
print_triangle(0, "")

print_triangle(6, "*")
print_triangle(6, "*")


# Задание 21
# Определите функцию fibonacci, принимающую один параметр:
# Имя
# sequence_number
# Тип
# Пример	входа
# int
# 4
# Функция должна вернуть число Фибоначчи с указанным поряд
# ковым номером (нумерация начинается с 0).
# Дополнительные условия:
# функция должна быть рекурсивной;

def fibonacci(sequence_number: int) -> int:
    if sequence_number == 0:
        return 0
    if sequence_number == 1:
        return 1
    return fibonacci(sequence_number - 1) + fibonacci(sequence_number - 2)


print(fibonacci(4))
print(fibonacci(0))
print(fibonacci(6))


# Задаача 22
# Гармонической суммой называется сумма чисел, обратных задан
# ным. Обратным числом называется результат деления 1 на это
# число. Например, обратным к 2 является 0.5, потому что 1, поде
# ленная на 2, равна 0.5.
# Обычно, говоря о гармонической сумме, имеют в виду множе
# ство натуральных чисел от 1 до n. Формула гармонической суммы
# n слагаемых имеет вид Hn = 1/1 + 1/2 + 1/3 + … + 1/n.
# Задание
# Определите функцию harmonic_sum, принимающую один параметр:
# Имя
# N
# Тип
# Пример	входа
# int
# 5
# Функция должна возвращать гармоническую сумму n слагаемых.
# Дополнительные условия:
# функция должна быть рекурсивной;

def harmonic_sum(n: int) -> float:
    if n <= 0:
        return 0
    return 1 / n + harmonic_sum(n - 1)


print(harmonic_sum(5))
print(harmonic_sum(2))
print(harmonic_sum(0))


# Задание 23
# Определите функцию xor, принимающую два параметра:
# Имя Тип Пример	входа
# input_a str "1101"
# input_b str "0001"
# Функция должна возвращать строку, являющуюся результатом
# применения XOR к двум входным строкам. Если одна строка длин
# нее другой, то лишние символы следует игнорировать.


def xor(input_a: str, input_b: str) -> str:
    len_str = min(len(input_a), len(input_b))
    anser_str = []
    for i in range(len_str):
        if input_a[i] == input_b[i]:
            anser_str.append("0")
        else:
            anser_str.append("1")
    return "".join(anser_str)


print(xor("1111", "1111"))
print(xor("1111", "0000"))
print(xor("1101", "00010"))

# Задача 24
# Определите функцию my_zip, принимающую два параметра:
# Имя
# input_list_a
# input_list_b
# Тип
# список Any
# Пример	входа
# [1, 2, 3, 4]
# список Any
# [5, 6, 7, 8]
# Функция должна возвращать такой же результат, как встроенная
# в Python функция zip.

from typing import Any


def my_zip(input_list_a: list[Any], input_list_b: list[Any]) -> list[tuple[Any, Any]]:
    len_list = min(len(input_list_a), len(input_list_b))
    zip_list = []
    for i in range(len_list):
        zip_list.append((input_list_a[i], input_list_b[i]))
    return zip_list


print(my_zip([1, 2, 3, 4], [5, 6, 7, 8]))
print(my_zip([], []))
print(my_zip([1, 2, 3], [5, 6, 7, 8]))


# Определите функцию is_valid_equation, принимающую один пара
# метр:
# Имя Тип Пример	входа Ограничение
# input_equation str "2 + 3 = 5"
# Строка должна состоять из целого
# числа, за которым следует знак
# плюс или минус, за ним еще
# одно целое число, знак равенства
# и ответ.
# Числа и знаки операций должны
# быть разделены пробелами
# Функция должна возвращать булево значение, показывающее,
# верно ли равенство. Равенство считается верным, если
# его формат совпадает с описанным выше;
# обе части равенства равны одному и тому же числу.

def is_valid_equation(input_equation: str) -> bool:
    result_of_operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "/": lambda a, b: round(a / b, 6),
        "*": lambda a, b: a * b,
    }
    list_of_numbers = input_equation.split()
    if (not list_of_numbers or
            len(list_of_numbers) != 5 or
            list_of_numbers[3] != "=" or
            list_of_numbers[1] not in result_of_operations):
        return False
    try:
        first_number = int(list_of_numbers[0])
        second_number = int(list_of_numbers[2])
        last_number = int(list_of_numbers[-1])
        operation = list_of_numbers[1]
    except ValueError:
        return False
    return result_of_operations[operation](first_number, second_number) == last_number


print(is_valid_equation("-5 - -3 = -2"))
print(is_valid_equation("5 - -5 = 10"))
print(is_valid_equation("-0 + 0 = 0"))
print(is_valid_equation("01 + 2 = 3"))
print(is_valid_equation("2 + 3= 5"))
print(is_valid_equation("2+ 3 = 5"))
print(is_valid_equation("2 +3 = 5"))
print(is_valid_equation("2 + 3 = 5 0"))

# Задание 26
# Определите функцию rotate_list_left, принимающую два параметра:
# Имя Тип Пример	входа
# rotate_amount
# int
# [1, 2, 3, 4, 5]
# 2
# Функция должна возвращать новый список, элементами которо
# го являются элементы исходного списка, циклически сдвинутые на
# заданное число позиций.
# Дополнительные условия:
# в решении не должны использоваться циклы;
# функция должна работать, даже если величина сдвига боль
# ше длины списка, например результат циклического сдвига
# на 6 должен порождать такой же результат, как циклический
# сдвиг на 1.

# ЗАДАЧУ СНИЗУ ТАК ЖЕ ПРОВЕРЬТЕ
from typing import Any


def rotate_list_right(input_list: list[Any], rotate_amount: int) -> list[Any]:
    rotate_amount %= len(input_list)
    return input_list[len(input_list) - rotate_amount:] + input_list[:len(input_list) - rotate_amount]


def rotate_list_left(input_list: list[Any], rotate_amount: int) -> list[Any]:
    rotate_amount %= len(input_list)
    return input_list[rotate_amount:] + input_list[:rotate_amount]


print(rotate_list_right([1, 2, 3, 4, 5], 2))
print(rotate_list_left([1, 2, 3, 4, 5], 5))
print(rotate_list_left([1, 2, 3, 4, 5], 8))


# Задение 27
# Определите функцию find_adjacent_nodes, принимающую два па
# раметра:
# Имя Тип
# adj_matrix список списков int
# start_node
# int
# Пример	входа
# [[1, 1, 1], [1, 0, 0], [1, 0, 0]]
# 0
# Функция должна возвращать список всех вершин, смежных со
# start_node.
# Эту задачу можно решить функцией, тело которой содержит все
# го одну строку. Сможете ли вы найти такое решение?


def find_adjacent_nodes(
        adj_matrix: list[list[int]],
        start_node: int
) -> list[int]:
    return [index for index in range(len(adj_matrix)) if adj_matrix[start_node][index] == 1]


print(find_adjacent_nodes([[1, 1, 1], [1, 0, 0], [1, 0, 0]], 0))
print(find_adjacent_nodes([[1, 1, 1], [1, 0, 0], [1, 0, 0]], 1))
print(find_adjacent_nodes([[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1,
                                                                      0]], 1))


# Задание 28
# Определите функцию count_peaks_valleys, принимающую один па
# раметр:
# Имя Тип Пример	входа
# price_action список int
# [1, 2, 3, 2, 1]
# Функция должна возвращать кортеж, показывающий, сколько
# имеется пиков и впадин в заданном движении цены. Кортеж дол
# жен содержать два целых числа, первое из которых равно числу
# пиков, а второе – числу впадин.


def count_peaks_valleys(price_action: list[int]) -> tuple[int, int]:
    peaks_valleys = [0, 0]
    for action in range(1, len(price_action) - 1):
        if price_action[action - 1] < price_action[action] > price_action[action + 1]:
            peaks_valleys[0] += 1
        elif price_action[action - 1] > price_action[action] < price_action[action + 1]:
            peaks_valleys[1] += 1
    return tuple(peaks_valleys)


print(count_peaks_valleys([1, 2, 3, 2, 1]))
print(count_peaks_valleys([1, 2, 3, 2, 1, 2]))
print(count_peaks_valleys([7, 6, 5, 10, 11, 12, 10, 9, 10]))
