# Task 1
import time
import datetime


class GameCharacter:
    def __init__(self, name, health, level):
        self.name = name
        self.__health = health
        self.level = level

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value > 100:
            value = 100
        self.__health = value

    def _level_up(self):
        self.level += 1

    def attack(self, other):
        other.health -= 10

    @classmethod
    def new_checker(cls):
        return cls(name="", health=100, level=1)

    @staticmethod
    def comparison_of_checker(char1, char2):
        return char1 if char1.level > char2.level else char2


# Task 2

class Store:
    def __init__(self, name, list_of_products=None):
        self.name = name
        self.products = list_of_products if list_of_products is not None else []

    def add_product(self, name, price, quantity):
        product_dict = {'name': name, 'price': price, 'quantity': quantity}
        self.products.append(product_dict)

    def remove_product(self, name):
        for index_product in range(len(self.products)):
            if self.products[index_product].get("name") == name:
                self.products.pop(index_product)

    def update_price(self, name, price):
        for product in self.products:
            if product.get("name") == name:
                product["price"] = price

    def sell_product(self, name, quantity):
        for product in self.products:
            if product.get("name") == name:
                if product["quantity"] - quantity < 0:
                    print("Нельзя продать столько товара")
                else:
                    product["quantity"] -= quantity

    def get_inventory(self):
        return (self.products, len(self.products))

    def find_most_expensive(self):
        max_product = None
        max_price = 0
        for product in self.products:
            if product["price"] > max_price:
                max_price = product["price"]
                max_product = product
        return max_product

    def find_cheapest(self):
        min_product = self.products[0]
        min_price = self.products[0].get("price")
        for product in self.products:
            if product["price"] < min_price:
                min_price = product["price"]
                min_product = product
        return min_product


# Task3

class Book:
    def __init__(self, title, author, year, status):
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def info(self):
        print(f"Name: {self.title}\nAuthor: {self.author}\nYear: {self.year}\nStatus: {self.status}")

    def mark_as_taken(self):
        self.status = "taken"

    def mark_as_returned(self):
        self.status = "returned"


class Library:
    def __init__(self, name, books=None):
        self.books = books if books is not None else []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def find_by_author(self, author):
        books_by_author = []
        for index in range(len(self.books)):
            if self.books[index].author == author:
                books_by_author.append(self.books[index])
        return books_by_author

    def find_by_year(self, year):
        books_by_year = []
        for index in range(len(self.books)):
            if self.books[index].year == year:
                books_by_year.append(self.books[index])
        return books_by_year

    def available_books(self):
        books_available = []
        for book in self.books:
            if book.status == "returned":
                books_available.append(book)
        return books_available

    def taken_books(self):
        books_taken = []
        for book in self.books:
            if book.status == "taken":
                books_taken.append(book)
        return books_taken


# Task4
class Wallet:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        self.__apply_bonus()

    def withdraw(self, amount):
        if amount > self._balance:
            print("Недостаточно средств")
        else:
            self._balance -= amount

    def transfer_to(self, other_wallet, amount):
        if amount > self._balance:
            print("Недостаточно средств")
        else:
            self._balance -= amount
            other_wallet.deposit(amount)

    def __apply_bonus(self):
        self._balance *= 1.01

    @property
    def balance(self):
        return self._balance

    @staticmethod
    def wallet_info(wallet):
        print(f"Balance: {wallet.balance}")


# Task5

class Order:
    def __init__(self, index=-1, items=None, status="new"):
        self.index = index
        self.items = items if items is not None else []
        self.status = status

    def calculate_total(self):
        return sum(map(lambda x: x.get("price") * x.get("quantity"), self.items))

    def add_item(self, name, price, quantity):
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def remove_item(self, name):
        for item in self.items:
            if item.get("name") == name:
                self.items.remove(item)

    def change_status(self, status):
        self.status = status

    def __str__(self):
        return f"Order #{self.index}: {self.status}"


class OrderSystem:
    def __init__(self, orders=None):
        self.orders = orders if orders is not None else []

    def create_order(self):
        self.orders.append(Order())

    def get_order_by_id(self, order_id):
        for order in self.orders:
            if order.index == order_id:
                return order

    def get_total_revenue(self):
        return sum([item.get("price") for order in self.orders for item in order.items if order.status == "returned"])

    def list_orders_by_status(self, status):
        return [order for order in self.orders if order.status == status]


# Task 6

class Car:
    def __init__(self, stamp, model, year, fuel=0, mileage=0):
        self.stamp = stamp
        self.model = model
        self.year = year
        self.fuel = fuel
        self.mileage = mileage

    def drive(self, distance):
        if self.__check_fuel(distance):
            self.mileage += distance
            self.fuil -= distance * 0.1
        else:
            print("Топлива не хватит")

    def refuel(self, liters):
        self.fuil += liters

    @property
    def age(self):
        return datetime.datetime.now().year - self.year

    def info(self):
        print(f"Stamp {self.stamp}\n"
              f"Model: {self.model}\n"
              f"Year: {self.year}\n"
              f"Fuel: {self.fuel}\n"
              f"Mileage: {self.mileage}\n")

    def __check_fuel(self, distance):
        spent_fuel = distance * 0.1
        return spent_fuel <= self.fuel

    @classmethod
    def from_string(cls, data):
        new_car = data.split(", ")
        new_car[2] = int(new_car[2])
        return cls(*new_car)


# Task 7

class Inventory:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def add_item(self, name, weight, value):
        self.items.append({"name": name, "weight": weight, "value": value})

    def remove_item(self, name):
        for item in self.items:
            if item.get("name") == name:
                self.items.remove(item)

    def get_total_weight(self):
        return sum([item.get("weight") for item in self.items])

    def get_total_value(self):
        return sum([item.get("value") for item in self.items])

    def find_heaviest(self):
        if not self.items:
            return None
        heaviest_item = self.items[0]
        heaviest_value = self.items[0].get("weight")
        for item in self.items:
            if item.get("weight") > heaviest_value:
                heaviest_value = item.get("weight")
                heaviest_item = item
        return heaviest_item

    def find_valuable(self):
        if not self.items:
            return None
        valuable_item = self.items[0]
        valuable_value = self.items[0].get("value")
        for item in self.items:
            if item.get("value") > valuable_value:
                valuable_value = item.get("value")
                valuable_item = item
        return valuable_item

    def sort_by_value(self):
        return sorted(self.items, key=lambda item: item.get("value"))

    def sort_by_weight(self):
        return sorted(self.items, key=lambda item: item.get("weight"))

#Task 8

class Gym:
    def __init__(self,name,clients = None):
        self.name = name
        self.clients = clients if clients is not None else []

    def add_client(self, name,age):
        self.clients.append({"name": name, "age": age,"status": False})

    def activate_client(self, name):
        for client in self.clients:
            if client["name"] == name:
                client["status"] = True

    def deactivate_membership(self, name):
        for client in self.clients:
            if client["name"] == name:
                client["status"] = False

    def get_active_members(self):
        return [client for client in self.clients if client["status"]]

    def find_youngest_member(self):
        youngest_member = self.clients[0]
        youngest_value = self.clients[0].get("age")
        for client in self.clients:
            if client["age"] < youngest_value:
                youngest_value = client["age"]
                youngest_member = client
        return youngest_member

    def find_oldest_member(self):
        oldest_member = self.clients[0]
        oldest_value = self.clients[0].get("age")
        for client in self.clients:
            if client["age"] > oldest_value:
                oldest_value = client["age"]
                oldest_member = client
        return oldest_member

    def  average_age(self):
        return sum([client["age"] for client in self.clients]) / len(self.clients)

# Task 9

class Playlist:
    def __init__(self, name, tracks=None):
        self.name = name
        self.tracks = tracks if tracks is not None else []

    def add_track(self, name, artist, duration):
        self.tracks.append({"name": name, "artist": artist, "duration": duration})

    def remove_track(self, name):
        for track in self.tracks:
            if track["name"] == name:
                self.tracks.remove(track)

    def total_duration(self):
        return sum([item.get("duration") for item in self.tracks])

    def find_by_artist(self, artist):
        all_tracks_artist = [track for track in self.tracks if track.get("artist") == artist]
        return all_tracks_artist

    def longest_track(self):
        return max(self.tracks, key=lambda item: item.get("duration"))

    def shortest_track(self):
        return min(self.tracks, key=lambda item: item.get("duration"))

    def shuffle(self):
        random.shuffle(self.tracks)

    def sort_by_duration(self, reverse=False):
        return sorted(self.tracks, key=lambda item: item.get("duration"), reverse=reverse)


# Task 10

class Student:
    def __init__(self, name, grades=None):
        self.name = name
        self.grades = grades if grades is not None else []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def info(self):
        print(f"Name: {self.name}\n"
              f"Grades: {self.grades}\n")


class StudyGroup:
    def __init__(self, name, students = None):
        self.name = name
        self.students = students if students is not None else []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)

    def find_best_student(self):
        return max(self.students,key = lambda student: student.average_grade())

    def group_average(self):
        if self.students is not None and len(self.students) > 0:
            return sum(map(lambda student: student.average_grade(),self.students)) / len(self.students)


    def list_student(self):
        for student in self.students:
            student.info()



