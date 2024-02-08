class Controller:
    def __init__(self):
        self.__account_list = []
        self.__promotion_list = []
        self.__product_list = []
        self.__history_order_list = []

    def add_account(self, account):
        self.__account_list.append(account)

    def add_product(self, product):
        self.__product_list.append(product)

    def get_user_by_username(self, username):
        for account in self.__account_list:
            if account.username == username:
                return account
            return None

    def validate_user_credentials(self, username, password):
        user = self.get_user_by_username(username)
        if user and user.password == password:
            return True
        return False

    def get_product(self):
        return self.__product_list


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



class Order:
    def __init__(self):
        pass