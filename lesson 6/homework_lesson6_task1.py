# 1. Напишите функцию root(x),
# которая возвращает квадрат своего аргумента
def root(x: int | float) -> int | None:
    if isinstance(x, int) or isinstance(x, float):
        return x ** 2


print(root(54))


# Напишите функцию is_even(n), которая проверяет, является ли число
# четным или нечетным. Функция должна возвращать True, если число четное,
# и False, если число нечетное.
def is_even(x: int | float) -> bool:
    if isinstance(x, int) or isinstance(x, float):
        return x % 2 == 0


print(is_even(53))


# Напишите функцию factorial(n), которая вычисляет факториал своего
# аргумента. Факториал числа n — это произведение всех натуральных чисел от
# 1 до n. Например, factorial(4) = 4×3×2×1 = 24.
# Функция должна возвращать факториал числа или -1, если число
# отрицательное

def factorial(x: int) -> int:
    if x < 0:
        return -1
    if x == 1:
        return 1
    return factorial(x - 1) * x


print(factorial(-52))


# Напишите функцию reverse(s), которая принимает строку s и возвращает
# ее в обратном порядке. Например, reverse("hello") должна вернуть
# "olleh".

def reverse(s: str) -> str:
    if isinstance(s, str):
        return s[::-1]


print(reverse("hello"))


#  Напишите функцию fibonacci(n), которая возвращает n-ый член
# последовательности Фибоначчи. Первые два числа равны 1.

def fibonacci(n: int) -> int | None:
    if isinstance(n, int):
        if n <= 0:
            return -1
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a


print(fibonacci(7))


# Напишите функцию count_vowels(s), которая подсчитывает количество
# гласных букв в строке s. Гласные буквы — это а, е, ё, и, о, у, ы, э, ю, я.
# Например, count_vowels("привет") должна вернуть 2.

def count_vowels(s: str) -> int | None:
    if isinstance(s, str):
        vowels = "а, е, ё, и, о, у, ы, э, ю, я".split(", ")
        count = 0
        for letter in s:
            if letter.lower() in vowels:
                count += 1
        return count


print(count_vowels("ПрИвУт"))


# Напишите функцию is_palindrome(s), которая проверяет, является ли
# строка s палиндромом.
# Палиндром — это слово или фраза, которая читается одинаково слева направо
# и справа налево. Функция должна возвращать True, если строка палиндром,
# и False, если нет

def is_palindrome(s: str) -> bool | None:
    if isinstance(s, str):
        return s == s[::-1]


print(is_palindrome("топот"))


# Напишите функцию power(x, n), которая возводит число x в степень n.
# Например, power(2, 3) должна вернуть 23 = 8.

def power(x: int | float, n: int) -> int | None:
    if (isinstance(x, int) or isinstance(x, float)) and isinstance(n, int):
        return x ** n


print(power(2, 3))


# . Напишите функцию is_anagram(s1, s2), которая проверяет, являются ли
# две строки s1 и s2 анаграммами.
# Анаграмма — это слово, составленное из перестановки букв другого слова.
# Функция должна возвращать True, если строки анаграммы, и False, если
# нет. Например, is_anagram("кот", "ток") должна вернуть True, а
# is_anagram("кот", "собака") должна вернуть False.

def is_anagram(s1: str, s2: str) -> bool | None:
    if isinstance(s1, str) and isinstance(s2, str):
        return set(s1) == set(s2) and len(s1) == len(s2)


print(is_anagram("трос", "сорт"))


# Напишите функцию is_pangram(s), которая проверяет, является ли строка
# s панграммой или нет.
# Панграмма — это строка, которая содержит все буквы алфавита хотя бы один
# раз. Функция должна возвращать True, если строка панграмма, и False, если
# нет.
# Например, is_pangram("Аэрофотосъёмка ландшафта уже выявила
# земли богачей и процветающих крестьян.") должна вернуть True,
# а is_pangram("Привет, мир") должна вернуть False.

def is_pangram(s: str) -> bool | None:
    all_letters = "а, б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я".split(
        ", ")
    print(all_letters)
    if isinstance(s, str):
        new_s = list()
        for letter in s:
            if letter.lower() in all_letters:
                new_s.append(letter.lower())
        return set(new_s) == set(all_letters)


print(is_pangram("Аэрофотосёмка ландшафта уже выявила земли богачей и процветающих крестьян."))
