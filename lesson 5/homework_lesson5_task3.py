# 2. Маша хочет накопить на телефон, который стоит N
# денег. Маша может откладывать k рублей каждый день,
# кроме воскресенья (в воскресенье она тратит эти деньги на
# поход в кино). Маша начинает копить в понедельник. За
# сколько дней она накопит нужную сумму?

n = int(input("Enter a number N: "))
k = int(input("Enter a number K: "))
sum = 0
index = 0
while sum != n:
    index += 1
    if index % 7 == 0:
        continue
    sum += k

print(index)

# Реализовать вывод последовательности чисел
# Фибоначчи (1 1 2 3 5 8 13 21 34 55 89 ...), где каждое
# следующее число является суммой двух предыдущих.

number = int(input("Сколько вывести чисел Фибоначи:\n"))

numbers_of_Febonachy = [0, 1]

for i in range(1, number - 1):
    numbers_of_Febonachy.append(numbers_of_Febonachy[i] + numbers_of_Febonachy[i - 1])

for i in numbers_of_Febonachy:
    print(i)

#########################3
