import math


class Controller:
    def __init__(self):
        self.__payment_list = []
        self.__account_list = []
        self.__promotion_list = []
        self.__product_list = []
        self.__history_order_list = []

    @property
    def payment_list(self):
        return self.__payment_list

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

    def get_last_history_id(self):
        histo_id = len(self.__history_order_list) + 1
        return histo_id

    def add_promotion(self, promotion):
        self.__promotion_list.append(promotion)

    def add_new_product(self, product):
        self.__product_list.append(product)

    def add_product_to_cart(self, username, product_id, quanity):
        account = self.search_account_by_username(username)
        cart = account.get_cart
        product = self.search_product_by_id(product_id)
        cart.add_product(
            Selected_product(
                product.product_id,
                product.name,
                product.price,
                product.category,
                product.color,
                product.picture,
                quanity,
            )
        )

    def add_account(self, account):
        self.__account_list.append(account)

    def add_payment(self, payment):
        self.__payment_list.append(payment)

    def add_history_order(self, order):
        pass
        # self.__history_order_list.append(Order())

    def remove_product(self, product_id):
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

    def search_payment_by_id(self, payment_id):
        for payment in self.__payment_list:
            if payment_id == payment.id:
                return payment

    def check_quanity_product(
        self, selected_product_list
    ):  ########################New method
        for selected_product in selected_product_list:
            for product in self.__product_list:
                if selected_product.quanity > product.quanity:
                    return False
        return True

    def calculate_order_price(self, total_price, promotion_id):
        promotion = self.search_promotion_by_id(promotion_id)
        discount = promotion.discount
        order_price = total_price - (total_price * (discount * 0.01))
        return order_price

    def create_order(self, username, address_id, promotion_id, payment_id):
        pass
        account = self.search_account_by_username(username)
        cart = account.get_cart
        selected_product_list = cart.show_selected_product_list
        check_selected_product = self.check_quanity_product(selected_product_list)
        if check_selected_product == True:
            order_id = self.get_last_history_id()
            payment = self.search_payment_by_id(payment_id)
            order_price = self.calculate_order_price(cart.total_price, promotion_id)
            address = account.search_address_by_id(address_id)
            order = Order(
                order_id,
                selected_product_list,
                order_price,
                payment,
                account,
                address,
                address.tel,
                None,
            )
            self.__history_order_list.append(order)
            return order
        return False

    @property
    def search_box_color(self):
        color_list = []
        for product in self.__product_list:
            if product.color not in color_list:
                color_list.append(product.color)
        return color_list

    @property
    def search_box_category(self):
        category_list = []
        for product in self.__product_list:
            if product.category not in category_list:
                category_list.append(product.category)
        return category_list


class Account:
    def __init__(self, name, tel, username, password):
        self.__name = name
        self.__tel = tel
        self.__username = username
        self.__password = password

    @property
    def name(self):
        return self.__name

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def tel(self):
        return self.__tel

    def account_type(self):
        pass

    def set_username(self, new_username):
        self.__username == new_username

    def self_password(self, new_password):
        self.__password == new_password


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

    @property
    def address_list(self):
        return self.__address_list

    def add_address(
        self,
        name,
        house_id,
        soi,
        sub_distric,
        distric,
        province,
        post_code,
        tel,
    ):
        address_id = len(self.__address_list) + 1
        self.__address_list.append(
            Address(
                address_id,
                name,
                house_id,
                soi,
                sub_distric,
                distric,
                province,
                post_code,
                tel,
            )
        )

    def search_address_by_id(self, address_id):
        for address in self.__address_list:
            if address.id == address_id:
                return address


class Address:
    def __init__(
        self,
        address_id,
        name,
        house_id,
        soi,
        sub_distric,
        distric,
        province,
        post_code,
        tel,
    ):
        self.__address_id = address_id
        self.__name = name
        self.__house_id = house_id
        self.__soi = soi
        self.__sub_distric = sub_distric
        self.__distric = distric
        self.__province = province
        self.__post_code = post_code
        self.__tel = tel

    @property
    def id(self):
        return self.__address_id

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
        product_alredy_incart = False
        for item in self.__selected_product_list:
            if selected_product.product_id == item.product_id:
                item.edit_quanity(selected_product.quanity)
                print(item.quanity)
                product_alredy_incart = True
        if product_alredy_incart == False:
            self.__selected_product_list.append(selected_product)

    def remove_selected_product(self, product_id):
        for selected_product in self.__selected_product_list:
            if selected_product.product_id == product_id:
                self.__selected_product_list.remove(selected_product)

    @property
    def total_price(self):
        total_price = 0
        for selected_product in self.__selected_product_list:
            total_price += selected_product.price * selected_product.quanity

        self.__total_price = total_price

        total_price = round(total_price, 2)
        return total_price

    @property
    def total_quantity(self):
        total_quantity = 0
        for selected_product in self.__selected_product_list:
            total_quantity += selected_product.quanity
        return total_quantity

    @property
    def show_selected_product_list(self):
        return self.__selected_product_list


class Selected_product(Product):
    def __init__(self, name, product_id, price, category, color, picture, quanity):
        super().__init__(name, product_id, price, category, color, picture, quanity)
        self.__quanity = quanity
        self.__total_price = price * quanity

    @property
    def quanity(self):
        return self.__quanity

    @property
    def total_price(self):
        return self.__total_price

    def edit_quanity(self, other):
        self.__quanity += other


class Promotion:
    def __init__(self, promotion_id, name, discount):
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
        selected_product_list,
        order_price,
        payment_type,
        account,
        address,
        tel,
        status,
    ):
        self.__order_id = order_id
        self.__selected_product_list = selected_product_list
        self.__order_price = order_price
        self.__payment_type = payment_type
        self.__account = account
        self.__address = address
        self.__tel = tel
        self.__status = status

    @property
    def id(self):
        return self.__order_id

    @property
    def selected_product_list(self):
        return self.__selected_product_list

    @property
    def order_price(self):
        return self.__order_price

    @property
    def payment_type(self):
        return self.__payment_type

    @property
    def account(self):
        return self.__account

    @property
    def address(self):
        return self.__address

    @property
    def tel(self):
        return self.__tel

    @property
    def status(self):
        return self.__status


class Payment:
    def __init__(self, payment_id, payment_type):
        self.__payment_id = payment_id
        self.__payment_type = payment_type

    @property
    def id(self):
        return self.__payment_id

    @property
    def payment_type(self):
        return self.__payment_type


#######################################
GRADE = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
GRADE = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
GRADE = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
GRADE = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
GRADE = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
GRADE = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
GRADE = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
GRADE = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
GRADE = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
GRADE = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
GRADE = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
GRADE = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
GRADE = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
GRADE = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
GRADE = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
