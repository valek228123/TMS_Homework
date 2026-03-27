from enum import StrEnum
from typing import Callable
from sqlalchemy import select
from .db_conector import session
from .models import Tickets, Products, User, Orders


class MenuCommandBeforeReg(StrEnum):
    show_products = "Товары"
    req = "Зарегистрироваться"
    login = "Войти"


class MenuCommandAfterReg(StrEnum):
    show_products = "Товары"
    pay_product = "Купить"
    view_profile = "Профиль"
    add_ticket = "Тикет"


class Menu:
    OPENING_STRING = """
   ===Добро пошаловать в "Не магазин"===

Здесь вы можете обменивать тикеты для того, чтобы приобретать товары

Для взаимодействия используйте команды:

{command}
"""

    def __init__(self):
        self._user: User | None = None
        self._command_before_req: dict[MenuCommandBeforeReg, Callable] = {}
        self._command_after_req: dict[MenuCommandAfterReg, Callable] = {}
        self._login: bool = False

    @staticmethod
    def show_products(*args, **kwargs) -> None:
        products = session.query(Products).all()
        print("ID    Стоимасть   Кол-во    Название\n=======================================")
        for product in products:
            print(f"{product.id:<6}{product.cost:<12}{product.count:<10}{product.name}")
        print()

    def req(self, *args, **kwargs) -> None:
        username = input("Введите логин > ")
        password = input("Введите пароль > ")
        if not username or not password:
            print("Имя или пароль не может быть пустым")
            return
        if username and User.is_exist(username):
            print("Пользователь с таким именем уже существует")
            return
        user = User(username=username, password=password)
        session.add(user)
        session.commit()
        print("Вы вошли в систему")
        self._login = True
        self._user = user
        print(Menu.OPENING_STRING.format(command=self.view_commands()))

    def login(self, *args, **kwargs) -> None:
        username = input("Введите логин > ")
        password = input("Введите пароль > ")
        if not username or not password:
            print("Имя или пароль не может быть пустым")
            return
        user = User.get_user_by_username(username=username)
        if not user:
            print("Пользователя с таким именем не существует")
            return
        if user and not user.check_password(password):
            print("Неправельный пароль")
            return
        print("Вы вошли в систему")
        self._login = True
        self._user = user
        print(Menu.OPENING_STRING.format(command=self.view_commands()))

    def pay_product(self, id_product: int, count_product: int, *args, **kwargs) -> None:
        id_product = int(id_product)
        count_product = int(count_product)
        product = Products.get_product_by_id(id_product)
        if not product:
            print("Продукт с таким id не найден")
            return
        if count_product < 0 or count_product > product.count:
            print("Количество не может быть отрецательным или больше чем есть на складе")
            return
        user_points = self._user.points
        all_cost = product.cost * count_product
        if all_cost > user_points:
            print("У вас не достаточно средст для покупки")
            return
        product.count -= count_product
        self._user.points -= all_cost
        print(f'Вы успешно купили "{product.name}" в количестве: {count_product}\n'
              f'У вас осталось - {self._user.points} поинтов')
        order = Orders(user_id=self._user.id, product_id=product.id, count=count_product)
        session.add(order)
        session.commit()

    def view_profile(self, *args, **kwargs) -> None:
        all_orders = Orders.get_orders_by_user_id(self._user.id)
        print(f"==={self._user.username}===\n"
              f"Поинтов: {self._user.points}\n\n"
              f"Заказы: \n")
        if not all_orders:
            print("Заказов пока нету")
            return
        print("Дата заказа    Кол-во    Сумма   Название\n=======================================")
        for order in all_orders:
            query = (
                select(Products.cost, Products.name)
                .join(Orders, Orders.product_id == Products.id)
                .where(Products.id == order.product_id)
            )
            product = session.execute(query).first()
            print(
                f"{order.order_datetime.strftime("%d/%m/%Y"):<15}{order.count:<10}{product[0] * order.count:<8}{product[1]}")

    def add_ticket(self, uuid, *args, **kwargs) -> None:
        ticket = Tickets.get_ticket_by_uuid(uuid=uuid)
        if not ticket:
            print("Такого тикета нету :(")
            return
        if not ticket.available:
            print("Этот тикет уже занят")
            return

        ticket.available = False
        ticket.user_id = self._user.id
        self._user.points += 20
        print("Вы успешно обменяли тикет на 20 поинтов\n"
              f"Теперь у вас {self._user.points}\n")
        session.commit()

    def add_command_before_reg(self) -> None:
        self._command_before_req[MenuCommandBeforeReg.show_products] = self.show_products
        self._command_before_req[MenuCommandBeforeReg.req] = self.req
        self._command_before_req[MenuCommandBeforeReg.login] = self.login

    def add_command_after_reg(self) -> None:
        self._command_after_req[MenuCommandAfterReg.show_products] = self.show_products
        self._command_after_req[MenuCommandAfterReg.pay_product] = self.pay_product
        self._command_after_req[MenuCommandAfterReg.view_profile] = self.view_profile
        self._command_after_req[MenuCommandAfterReg.add_ticket] = self.add_ticket

    def view_commands(self) -> None:
        if not self._login:
            text = ""
            for cmd in self._command_before_req.keys():
                text += f"> {cmd}\n"
            return text
        else:
            text = ""
            for cmd in self._command_after_req.keys():
                text += f"> {cmd}\n"
            return text

    def run(self):
        self.add_command_before_reg()
        self.add_command_after_reg()
        print(Menu.OPENING_STRING.format(command=self.view_commands()))
        while True:
            try:
                input_str = input(f"[{self._user.username}]> " if self._user is not None else "> ").strip().split()
                cmd = input_str.pop(0)

                if not cmd and cmd not in MenuCommandBeforeReg and cmd not in MenuCommandAfterReg:
                    print("Нету такой команды")
                    continue
                if not self._login:
                    self._command_before_req.get(cmd)(*input_str)
                elif self._login:
                    self._command_after_req.get(cmd)(*input_str)
            except Exception as e:
                print(f"Ошибка! Попробуйте еще!\n")
