# Текст должен располагаться
# по средине
# Длина шапки всегда равна 30 символов, если предложение слишком длинное, то
# обрезать его.

string = input("Enter a string: ")
print("=" * 30)

print(string[:30].center(30))

print("=" * 30)

# Напишите программу, которая считывает три числа и подсчитывает сумму только
# положительных чисел

number_a = int(input("Enter a number 1: "))
number_b = int(input("Enter a number 2: "))
number_c = int(input("Enter a number 3: "))

sum = ((number_a if number_a > 0 else 0) +
       (number_b if number_b > 0 else 0) +
       (number_c if number_c > 0 else 0))

print(sum)

# Напишите программу, которая определяет, является ли год с данным номером
# високосным.
# Если год является високосным, то выведите «Да», иначе выведите «Нет».

year = int(input("Enter a year: "))

if year % 4 == 0 and year % 100 != 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# На вход программе подаются две клетки шахматной доски в формате «а7» «e3».
# Значение клетки необходимо считывать за один input.
# Напишите программу, которая определяет, может ли ладья попасть с первой
# клетки на вторую одним ходом.
# Программа должна вывести «Да», если из первой клетки ходом ладьи можно
# попасть во вторую, или «Нет» в противном случае.

string1 = input("Enter a string: ")
string2 = input("Enter a string: ")

if string1[0] == string2[0] or string1[-1] == string2[-1]:
    print("Yes")
else:
    print("No")
