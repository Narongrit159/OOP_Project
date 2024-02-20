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

    chick_shop.add_payment(Payment(1, "Internet Banking"))
    chick_shop.add_payment(Payment(2, "Online Direct Debit"))
    chick_shop.add_payment(Payment(3, "Bill Payment "))

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
    chick_shop.add_new_product(
        Product(
            7,
            "Hoodies White Gray",
            8.99,
            "Hoodies",
            "Gray",
            "img/Hoodie-1 (gray).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            8,
            "Charles Hoodies Blue",
            14.99,
            "Hoodies",
            "Blue",
            "img/Hoodie-2 (blue).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            9,
            "Charles Hoodies Green",
            14.99,
            "Hoodies",
            "Green",
            "img/Hoodie-3 (green).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            10,
            "Charles Hoodies Orange",
            14.99,
            "Hoodies",
            "Orange",
            "img/Hoodie-4 (orange).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            11,
            "Charles Wilson Hoodies Green ",
            14.99,
            "Hoodies",
            "Green",
            "img/Hoodie-5 (green).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            12,
            "Hoodies Cream Brown",
            14.99,
            "Hoodies",
            "Brown",
            "img/Hoodie-6 (brown).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            13,
            "Hoodies Brown",
            14.99,
            "Hoodies",
            "Brown",
            "img/Hoodie-7 (brown).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            14,
            "Hoodies ZIP Red",
            14.99,
            "Hoodies",
            "Red",
            "img/Hoodie-8 (red).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            15,
            "Hood ZIP Gray",
            14.99,
            "Hoodies",
            "Gray",
            "img/Hoodie-9 (gray).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            16,
            "NIKE Hood Red",
            14.99,
            "Hoodies",
            "Red",
            "img/Hoodie-10 (red).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            17,
            "Avenger Blue Hoodies",
            14.99,
            "Hoodies",
            "Blue",
            "img/Hoodie-11 (blue).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            18,
            "White POLO",
            14.99,
            "Polo",
            "White",
            "img/Polo-1 (white).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            19,
            "Blue POLO",
            14.99,
            "Polo",
            "Blue",
            "img/Polo-2 (blue).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            20,
            "Blue & Orange POLO",
            14.99,
            "Polo",
            "Blue",
            "img/Polo-3 (blue).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            21,
            "Orange POLO",
            14.99,
            "Polo",
            "Orange",
            "img/Polo-4 (Orange).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            22,
            "Pink POLO",
            14.99,
            "Polo",
            "Pink",
            "img/Polo-5 (pink).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            23,
            "Hawk Blue POLO",
            14.99,
            "Polo",
            "Blue",
            "img/Polo-6 (blue).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            24,
            "Men Blue POLO",
            14.99,
            "Polo",
            "Blue",
            "img/Polo-7 (blue).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            25,
            "Black & White POLO",
            14.99,
            "Polo",
            "White",
            "img/Polo-8 (white).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            26,
            "Deer White POLO",
            14.99,
            "Polo",
            "White",
            "img/Polo-9 (white).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            27,
            "White Shirt",
            14.99,
            "Shirt",
            "White",
            "img/Shirt-1 (white).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            28,
            "Blue Shirt",
            14.99,
            "Shirt",
            "Blue",
            "img/Shirt-2 (blue).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            29,
            "Pink Shirt",
            14.99,
            "Shirt",
            "Pink",
            "img/Shirt-3 (pink).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            30,
            "GreenShirt",
            14.99,
            "Shirt",
            "Green",
            "img/Shirt-4 (green).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            31,
            "Red Shirt",
            14.99,
            "Shirt",
            "Red",
            "img/Shirt-5 (red).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            32,
            "Men Red Shirt",
            14.99,
            "Shirt",
            "Pink",
            "img/Shirt-6 (red).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            33,
            "Black Shirt",
            14.99,
            "Shirt",
            "Black",
            "img/Shirt-7 (Black).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            34,
            "White Shirt 2 Botton style",
            14.99,
            "Shirt",
            "White",
            "img/Shirt-8 (white).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            35,
            "Blown Sweater",
            14.99,
            "Sweater",
            "Brown",
            "img/Sweater-1 (brown).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            36,
            "Black Sweater",
            14.99,
            "Sweater",
            "Black",
            "img/Sweater-2 (black).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            37,
            "Gray Sweater",
            14.99,
            "Sweater",
            "Gray",
            "img/Sweater-3 (gray).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            38,
            "Blue Sweater",
            14.99,
            "Sweater",
            "Blue",
            "img/Sweater-4 (blue).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            39,
            "White Sweater",
            14.99,
            "Sweater",
            "White",
            "img/Sweater-5 (white).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            40,
            "Cotton Red Sweater",
            14.99,
            "Sweater",
            "Red",
            "img/Sweater-6 (red).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            41,
            "Fit Red Sweater",
            14.99,
            "Sweater",
            "Red",
            "img/Sweater-7 (red).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            42,
            "Fit Brown Sweater",
            14.99,
            "Sweater",
            "Brown",
            "img/Sweater-8 (brown).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            43,
            "Fit Blue Sweater",
            14.99,
            "Sweater",
            "Blue",
            "img/Sweater-10 (blue).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            44,
            "England Blue Sweater Style",
            14.99,
            "Sweater",
            "Blue",
            "img/Sweater-11 (blue).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            45,
            "Black & Brown Sweater",
            14.99,
            "Sweater",
            "Black",
            "img/Sweater-12 (black).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            46,
            "Green Sweater",
            14.99,
            "Sweater",
            "Green",
            "img/Sweater-13 (green).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            47,
            "Fit Blue T-Shirt",
            14.99,
            "T-Shirt",
            "Blue",
            "img/T-Shirt-1 (blue).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            47,
            "Fit Blue T-Shirt",
            14.99,
            "T-Shirt",
            "Blue",
            "img/T-Shirt-1 (blue).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            48,
            "Brown T-Shirt",
            14.99,
            "T-Shirt",
            "Brown",
            "img/T-Shirt-2 (brown).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            49,
            "White Sport T-Shirt",
            14.99,
            "T-Shirt",
            "White",
            "img/T-Shirt-3 (white).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            50,
            "Orange T-Shirt",
            14.99,
            "T-Shirt",
            "Orange",
            "img/T-Shirt-4 (orange).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            51,
            "Ping T-Shirt",
            14.99,
            "T-Shirt",
            "Pink",
            "img/T-Shirt-5 (pink).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            52,
            "Red T-Shirt",
            14.99,
            "T-Shirt",
            "Red",
            "img/T-Shirt-6 (red).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            53,
            "Blue T-Shirt",
            14.99,
            "T-Shirt",
            "Blue",
            "img/T-Shirt-7 (blue).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            54,
            "White Blue T-Shirt",
            14.99,
            "T-Shirt",
            "Blue",
            "img/T-Shirt-8 (blue).png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            55,
            "Black T-Shirt",
            14.99,
            "T-Shirt",
            "Black",
            "img/T-Shirt-9 (black).png",
            10,
        )
    )

    chick_shop.add_product_to_cart("chicken", 1, 2)
    chick_shop.add_product_to_cart("chicken", 2, 2)
    chick_shop.add_product_to_cart("chicken", 3, 2)
