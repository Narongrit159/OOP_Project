from models import (
    Product,
    Controller,
    Custumer_account,
    Owner_account,
    Cart,
    Payment,
    Promotion,
)

chick_shop = Controller()


def get_chick_shop_controller():
    return chick_shop


def create_new_instances():
    chicken_account = Custumer_account(
        "CHICKEN", "0620538988", "chicken", "0000", cart=Cart()
    )
    tar_account = Custumer_account("TAR", "0620538988", "tar", "0000", cart=Cart())
    maysa_account = Custumer_account(
        "MAYSA", "0620538988", "maysa", "0000", cart=Cart()
    )
    admin_account = Owner_account("ADMIN", "0", "admin", "0000", "0278645215")

    chicken_account.add_address(
        "NARONGRIT KAJEEJIT",
        "105/5",
        "",
        "MaeHia",
        "Muang Chiangmai",
        "Chiangmai",
        "50200",
        "0620538988",
    )
    chicken_account.add_address(
        "NARONGRIT KAJEEJIT (SJ HOUSE)",
        "105/5",
        "Ladkrabang 52",
        "Ladkrabang",
        "Ladkrabang",
        "Bangkok",
        "10520",
        "0620538988",
    )
    tar_account.add_address(
        "TEERACHART SUTTI",
        "105/5",
        "",
        "MaeHia",
        "Muang Chiangmai",
        "Chiangmai",
        "50200",
        "0923391646",
    )
    tar_account.add_address(
        "TEERACHART SUTTI",
        "105/5",
        "Ladkrabang 50/2",
        "Ladkrabang",
        "Ladkrabang",
        "Bangkok",
        "50200",
        "0923391646",
    )
    maysa_account.add_address(
        "CHANAKAN SUESUWAN",
        "1",
        "Chalong Krung 1 Alley",
        "Ladkrabang",
        "Khet Lat Krabang",
        "Krung Thep Maha Nakhon",
        "10520",
        "0923391646",
    )

    chick_shop.add_payment(Payment(1, "Paypal"))
    chick_shop.add_payment(Payment(2, "Card"))
    chick_shop.add_payment(Payment(3, "Bobile Banking"))

    chick_shop.add_promotion(Promotion(1, "New customer discount", 5))
    chick_shop.add_promotion(Promotion(2, "Songkran Festival discount", 10))
    chick_shop.add_promotion(Promotion(3, "Special discount for women", 30))

    chick_shop.add_account(chicken_account)
    chick_shop.add_account(tar_account)
    chick_shop.add_account(maysa_account)
    chick_shop.add_account(admin_account)

    chick_shop.add_new_product(
        Product(
            1,
            "Windbreaker Hood",
            14.99,
            "Hoodies",
            "Red",
            "img/new-1.png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            2,
            "Air Jordan Zipper",
            11.99,
            "Hoodies",
            "Black",
            "img/new-2.png",
            10,
        )
    )

    chick_shop.add_new_product(
        Product(
            3,
            "Fur Jacket",
            4.99,
            "Sweatter",
            "Yellow",
            "img/new-3.png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            4,
            "Fleece Jacket",
            24.99,
            "Sweatter",
            "White",
            "img/new-4.png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            5,
            "Red Shirt",
            7.99,
            "T-Shirt",
            "Red",
            "img/new-5.png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            6,
            "Nike Hoodies",
            5.99,
            "Hoodies",
            "White",
            "img/new-6.png",
            10,
        )
    )

    chick_shop.add_product_to_cart("chicken", 1, 2)
    chick_shop.add_product_to_cart("chicken", 2, 2)
    chick_shop.add_product_to_cart("chicken", 3, 2)
