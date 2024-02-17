class Controller:
    def __init__(self):
        self.__payment_list = []
        self.__account_list = []
        self.__promotion_list = []
        self.__product_list = []
        self.__history_order_list = []

    @property
    def get_product_list(self):
        return self.__product_list

    @property
    def get_promotion_list(self):
        return self.__promotion_list

    @property
    def account_list(self):
        return self.__account_list

    @property
    def promotion_list(self):
        return self.__promotion_list

    @property
    def history_order_list(self):
        return self.__history_order_list

    def get_cart_from_account(self, username):
        account = self.search_account_by_username(username)
        return account.get_cart

    def add_product(self, product):  ################น่าจะเปลี่ยน add_product_by_owner
        self.__product_list.append(product)

    def get_last_histo_id(self):
        histo_id = len(self.__history_order_list) + 1
        return histo_id

    def add_product_to_cart(self, username, product_id, quanity):  ############ต้าทำ
        account = self.search_account_by_username(username)
        cart = account.get_cart
        product = self.search_product_by_id(product_id)
        cart.add_product(Selected_product(product, quanity))

    def add_account(self, account):
        self.__account_list.append(account)

    def add_payment(self, payment):
        self.__payment_list.append(payment)

    def remove_product(
        self, product_id
    ):  #################น่าจะเปลี่ยนเป็นremove_product_by_owner
        product = self.search_product_by_id(product_id)
        self.__product_list.remove(product)

    def remove_promotion(self, promotion_id):
        promotion = self.search_promotion_by_id(promotion_id)
        self.__promotion_list.remove(promotion)

    def remove_product_from_cart(self, username, product_id):
        account = self.search_account_by_username(username)
        cart = account.get_cart
        cart.remove_selected_product(product_id)

    def show_cart(self, username):  ##############################ของกุ๊ก  ต้าทำ
        account = self.search_account_by_username(username)
        cart = account.get_cart
        return cart

    def calculate_order_price(self, username):
        pass

    def search_account_by_name(self, name):
        for account in self.__account_list:
            if account.name == name:
                return account

    def search_account_by_username(self, username):
        for account in self.__account_list:
            if account.username == username:
                return account
        return None

    def search_product_by_id(self, id):
        for product in self.__product_list:
            if product.product_id == id:
                return product

    def search_product_by_name(self, name):
        for product in self.__product_list:
            if product.name == name:
                return product

    def search_product_by_category(self, category):
        product_list = []
        for product in self.__product_list:
            if product.category == category:
                product_list.append(product)
            return product_list

    def search_product_by_color(self, color):
        product_list = []
        for product in self.__product_list:
            if product.color == color:
                product_list.append(product)
            return product_list

    def search_promotion_by_id(self, promotion_id):
        for promotion in self.__promotion_list:
            if promotion.promotion_id == promotion_id:
                return promotion

    def add_history_order(self, order):
        pass
        # self.__history_order_list.append(Order())


class Account:
    def __init__(self, name, tel, username, password):
        self.__name = name
        self.__tel = tel
        self.__username = username
        self.__password = password

    def account_type(self):
        pass

    def set_username(self, new_username):
        self.__username == new_username

    def self_password(self, new_password):
        self.__password == new_password

    @property
    def name(self):
        return self.__name

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password


class Owner_account(Account):
    def __init__(self, name, tel, username, password, bank_account):
        super().__init__(name, tel, username, password)
        self.__bank_account = bank_account

    @property
    def get_bank_account(self):
        return self.__bank_account


class Custumer_account(Account):
    def __init__(self, name, tel, username, password, cart):
        super().__init__(name, tel, username, password)
        self.__cart = cart
        self.__address_list = []

    @property
    def get_cart(self):
        return self.__cart

    def add_address(
        self, name, house_id, soi, sub_distric, distric, province, post_code, tel
    ):
        self.__address_list.append(
            Address(name, house_id, soi, sub_distric, distric, province, post_code, tel)
        )


class Address:
    def __init__(
        self, name, house_id, soi, sub_distric, distric, province, post_code, tel
    ):
        self.__name = name
        self.__house_id = house_id
        self.__soi = soi
        self.__sub_distric = sub_distric
        self.__distric = distric
        self.__province = province
        self.__post_code = post_code
        self.__tel = tel

    @property
    def name(self):
        return self.__name

    @property
    def house_id(self):
        return self.__house_id

    @property
    def soi(self):
        return self.__soi

    @property
    def sub_distric(self):
        return self.__sub_distric

    @property
    def distric(self):
        return self.__distric

    @property
    def provice(self):
        return self.__province

    @property
    def post_code(self):
        return self.__post_code

    @property
    def tel(self):
        return self.__tel


class Product:
    def __init__(self, product_id, name, price, category, color, picture, quanity):
        self.__name = name
        self.__product_id = product_id
        self.__color = color
        self.__picture = picture
        self.__category = category
        self.__quanity = quanity
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def product_id(self):
        return self.__product_id

    @property
    def color(self):
        return self.__color

    @property
    def picture(self):
        return self.__picture

    @property
    def quanity(self):
        return self.__quanity

    @property
    def price(self):
        return self.__price

    @property
    def category(self):
        return self.__category


class Cart:
    def __init__(self):
        self.__total_price = 0
        self.__selected_product_list = []

    def add_product(self, selected_product):
        self.__selected_product_list.append(selected_product)

    def remove_selected_product(self, product_id):
        for selected_product in self.__selected_product_list:
            if selected_product.product.product_id == product_id:
                self.__selected_product_list.remove(selected_product)

    @property
    def total_price(self):
        for selected_product in self.__selected_product_list:
            self.__total_price += (
                selected_product.product.price * selected_product.quanity
            )

        return self.__total_price

    @property
    def total_quantity(self):
        total_quantity = 0
        for selected_product in self.__selected_product_list:
            total_quantity += selected_product.quanity
        return total_quantity

    @property
    def show_selected_product_list(self):
        return self.__selected_product_list


class Selected_product:
    def __init__(self, product, quanity):
        self.__product = product
        self.__quanity = quanity

    @property
    def product(self):
        return self.__product

    @property
    def quanity(self):
        return self.__quanity


class Promotion:
    def __init__(self, name, promotion_id, discount):
        self.__promotion_name = name
        self.__promotion_id = promotion_id
        self.__dicount = discount

    @property
    def promotion_name(self):
        return self.__promotion_name

    @property
    def promotion_id(self):
        return self.__promotion_id

    @property
    def discount(self):
        return self.__dicount


class Order:
    def __init__(
        self,
        order_id,
        product_list,
        order_price,
        payment_type,
        account,
        address,
        tel,
        status,
    ):
        self.__order_id = order_id
        self.__product_list = product_list
        self.__order_price = order_price
        self.__payment_type = payment_type
        self.__account = account
        self.__address = address
        self.__tel = tel
        self.__status = status

    @property
    def order_id(self):
        return self.__order_id


class Payment:
    def __init__(self, payment_id, payment_type, discount):
        self.__payment_id = payment_id
        self.__payment_type = payment_type
        self.__discount = discount

    @property
    def get_id(self):
        return self.__payment_id

    @property
    def get_payment_type(self):
        return self.__payment_type

    @property
    def get_discount(self):
        return self.__discount


#######################################
a = 2
