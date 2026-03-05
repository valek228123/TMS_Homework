# Напишите программу, которая принимает на вход список чисел и выводит на
# экран сумму всех элементов списка.
# Используйте цикл while и переменную-счетчик.

list = input().split()
sum = 0

while list:
    sum += int(list.pop())

print(sum)

# 2. Напишите программу, которая принимает на вход строку и выводит на экран
# количество гласных букв в ней.
# Гласными буквами считаются “а”, “е”, “и”, “о”, “у”, “ы”, “э”, “ю”, “я”.
# Используйте цикл while.

glas = "аеиоуыэюя"
string = input()
index = 0
count = 0
while len(string) > index:
    if string[index] in glas:
        count += 1
    index += 1

print(count)

# 3. Напишите программу, которая принимает на вход список слов и выводит на
# экран самое длинное слово из списка и его длину.
# Если таких слов несколько, выведите первое из них.
# Используйте цикл while и переменные для хранения
# максимальной длины и самого длинного слова.

string = input().split()

max_string = ""
while string:
    world = string.pop()
    if len(max_string) < len(world):
        max_string = world

print(max_string, len(max_string))

# 4. Напишите программу, которая принимает на вход список чисел и выводит на
# экран новый список, в котором все четные числа умножены на 2, а все нечетные
# остались без изменений.
# Используйте цикл while и оператор %
# для определения четности числа.

string = input().split()
index = 0
new_list = []
while len(string) > index:
    if int(string[index]) % 2 == 0:
        new_list.append((int(string[index]) * 2))
    else:
        new_list.append((int(string[index])))
    index += 1

print(new_list)

# 5. Напишите программу, которая принимает на вход список чисел и выводит на
# экран индекс и значение минимального элемента в списке.
# Если таких элементов несколько, выведите первый индекс из них.
# Используйте цикл while и переменные
# для хранения минимального значения и его индекса.

string = input().split()
index = 0
min_index = 0
min_value = int(string[0])

while len(string) - 1 >= index:
    if int(string[index]) < min_value:
        min_value = int(string[index])
        min_index = index
    index += 1

print(min_index, min_value)

# 6. Напишите программу, которая принимает на вход строку и выводит на экран
# новую строку, в которой все слова записаны в обратном порядке.
# Например, строка “Привет, мир!” должна превратиться в “мир! Привет,”.
# Используйте цикл while и метод split()
# для разбиения строки на слова
# и метод join() для объединения слов в строку.

string = input().split()
new_string = []
index = len(string) - 1
while index >= 0:
    new_string.append(string[index])
    index -= 1

print(" ".join(new_string))
