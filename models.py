from typing import Set


class Controller:
    def __init__(self):
        self.__account_list = []
        self.__promotion_list = []
        self.__product_list = []
        self.__history_order_list = []

    def add_account(self, account):
        self.__account_list.append(account)

    def add_account(self, account):
        self.__account_list.append(account)

    def add_product(self, product):
        self.__product_list.append(product)

    def get_account_by_username(self, username):
        for account in self.__account_list:
            if account.username == username:
                return account
        return None

    def get_product(self):
        return self.__product_list

    def search_product_by_id(self, id):
        for product in self.__product_list:
            if product.product_id == id:
                return product

    def add_user_session(self, username):
        self.__user_sessions.add(username)

    def remove_user_session(self, username):
        self.__user_sessions.remove(username)


class Account:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password


class Product:
    def __init__(self, id, name, price, catagory, color, picture, quanity):
        self.__product_id = id
        self.__color = color
        self.__name = name
        self.__price = price
        self.__catagory = catagory
        self.__picture = picture
        self.__quanity = quanity

    @property
    def product_id(self):
        return self.__product_id

    @property
    def color(self):
        return self.__color

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def catagory(self):
        return self.__catagory

    @property
    def picture(self):
        return self.__picture


class Cart:
    def __init__(self):
        self.__selected_product_list = []
        self.__total_price = None

    def add_product_to_cart(self, controller, product_id):
        product = controller.search_product_by_id(product_id)
        self.__selected_product_list.append(product)

    def remove_selected_product(self, product_id):
        for product in self.__selected_product_list:
            if product.product_id == product_id:
                self.__selected_product_list.remove(product)

    def calculate_total_prize(self):
        for product in self.__selected_product_list:
            for product_price in product.price:
                self.__total_price += product_price

    @property
    def show_selected_product_list(self):
        return self.__selected_product_list

    @property
    def show_total_price(self):
        return self.__total_price


class Promotion:
    def __init__(self, name, promotion_id, discount_price):
        self.__promotion_name = name
        self.__promotion_id = promotion_id
        self.__dicount_price = discount_price

    @property
    def promotion_name(self):
        return self.__promotion_name

    @property
    def promotion_id(self):
        return self.__promotion_id

    @property
    def discount(self):
        return self.__dicount_price


class Order:
    def __init__(self, order_id, cart, account, address, tel, status):
        self.__order_id = order_id
        self.__cart = cart
        self.__account = account
        self.__address = address
        self.__tel = tel
        self.__status = status


class LoginInfo(Account):
    username: str
    password: str
