# Дан список чисел. С помощью map() получить список,
# где каждое число из исходного списка переведено в строку.
# Пример: на входе – [1, 2, 3], на выходе – [‘1’, ‘2’, ‘3’]

list1 = [1, 2, 3]
print(list(map(str, list1)))

# 2. Дан список чисел. С помощью filter() получить список
# тех элементов из исходного списка, значение которых
# больше 0.

list1 = [1, 2, 3, -1, 2, -2, 4, 5, -6, 7]
print(list(filter(lambda x: x > 0, list1)))
# 3. Дан список строк. С помощью filter() получить список
# тех строк из исходного списка, которые являются
# палиндромами (читаются в обе стороны одинаково, например,
# ’abcсba’)

list1 = ["abccba", "bacdcba", "bacdcba", "топот", "asdasd", "asfasfasfwq"]
print(list(filter(lambda x: x == x[::-1], list1)))

# Сделать декоратор, который измеряет время,
# затраченное на выполнение декорируемой функции.
import time


def time1(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{end - start} seconds")
        return res

    return wrapper


@time1
def func1():
    time.sleep(2)
    print("Функция работает")


func1()

# Используя map() и reduce() посчитать площадь
# квартиры, имея на входе характеристики комнат квартиры.
# Пример входных данных:

from functools import reduce

rooms = [
    {"name": "Kitchen", "length": 6, "width": 4},
    {"name": "Room 1", "length": 5.5, "width": 4.5},
    {"name": "Room 2", "length": 5, "width": 4},
    {"name": "Room 3", "length": 7, "width": 6.3}]

res = reduce(lambda x, y: x + y, map(lambda x: x.get("length") * x.get("width"), rooms))
print(res)
