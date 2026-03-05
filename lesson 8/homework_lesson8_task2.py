# 1 Реализовать программу для подсчёта индекса массы
# тела человека. Пользователь вводит рост и вес с клавиатуры.
# На выходе – ИМТ и пояснение к нему в зависимости от
# попадания в тот или иной диапазон. Использовать обработку
# исключений.

def calculation_bmi(weight: float, height: float) -> float:
    return weight / ((height / 100) ** 2)


def calculation_BMI() -> None:
    ranges_of_BMI = {
        (0, 18.5): "Недостаточная (дефицит) масса тела.",
        (18.5, 24.9): "Нормальная масса тела.",
        (25.0, 29.9): "Избыточная масса тела (предожирение).",
        (30, 34.9): "Ожирение I степени.",
        (35.0, 39.9): "Ожирение II степени.",
        (40.0, 10000): "Ожирение III степени (морбидное/суперожирение)."
    }
    while True:
        try:
            weight = float(input("Введите свой вес(кг): "))
            height = float(input("Введите свой рост(см): "))
            if weight <= 0 or height <= 0:
                raise ValueError("Рост или вес не могут быть отрицательными!")
            bmi = calculation_bmi(weight, height)
            for (low, hight), val in ranges_of_BMI.items():
                if low <= bmi <= hight:
                    print(f"{bmi:.1f}: {val}")
                    break
            else:
                print("Вы вряд ли человек :)")
        except ValueError as e:
            print(f"Ошибка - {e}")
        else:
            break


# 2. Реализовать программу с функционалом калькулятора
# для операций над двумя числами. Числа и операция вводятся
# пользователем с клавиатуры. Использовать обработку
# исключений
def calculation() -> None:
    LIST_OF_OPERATIONS = ["+", "-", "/", "*"]
    flag = True
    result_of_operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "/": lambda a, b: round(a / b, 6),
        "*": lambda a, b: a * b,
    }
    while flag:
        try:
            a, b = map(int, input("Введите два числа для опирации(через пробел): ").split())
            operation = input("Введите опирацию(+  -  / *): ")
            assert operation in LIST_OF_OPERATIONS, "Нету такой опирации, попробуй снова"

            print(f"Результат операции: {a} {operation} {b} = {result_of_operations[operation](a, b)}")

            while True:
                try:
                    inp = input("Еще раз?) (y - да, n - нет): ")
                    if inp.lower() not in ["y", "n"]:
                        raise ValueError("Введите да(y) или нет(n)")
                    if inp.lower() == "n":
                        flag = False
                        break
                except ValueError as e:
                    print(f"Ошибка - {e} TypeError")
                else:
                    break
        except ValueError as e:
            print(f"Ошибка - {e}")
        except ZeroDivisionError:
            print(f"На 0 делить нельзя!!!")
        except AssertionError as e:
            print("Введина неверная операция")


calculation()
