# main.py
import uvicorn
from fastapi import FastAPI, Depends, HTTPException, Form, Cookie, status, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from models import (
    Product,
    Controller,
    Custumer_account,
    Owner_account,
    Cart,
    Payment,
    Promotion,
)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")
templates = Jinja2Templates(directory="templates")

chick_shop = Controller()


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
            "Windbreaker Jacket",
            14.99,
            "Accessory",
            "red",
            "img/new-1.png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            2,
            "Air Jordan Zipper",
            11.99,
            "Accessory",
            "red",
            "img/new-2.png",
            10,
        )
    )

    chick_shop.add_new_product(
        Product(
            3,
            "Fur Jacket",
            4.99,
            "Accessory",
            "red",
            "img/new-3.png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            4,
            "Fleece Jacket",
            24.99,
            "Accessory",
            "red",
            "img/new-4.png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            5,
            "Nike Hoodie",
            7.99,
            "Accessory",
            "red",
            "img/new-5.png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            6,
            "Fleece Jacket",
            5.99,
            "Accessory",
            "red",
            "img/new-6.png",
            10,
        )
    )

    chick_shop.add_new_product(
        Product(
            7,
            "Windbreaker Jacket",
            14.99,
            "Accessory",
            "red",
            "img/new-1.png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            8,
            "Air Jordan Zipper",
            11.99,
            "Accessory",
            "red",
            "img/new-2.png",
            10,
        )
    )

    chick_shop.add_new_product(
        Product(
            9,
            "Fur Jacket",
            4.99,
            "Accessory",
            "red",
            "img/new-3.png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            10,
            "Fleece Jacket",
            24.99,
            "Accessory",
            "red",
            "img/new-4.png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            11,
            "Nike Hoodie",
            7.99,
            "Accessory",
            "red",
            "img/new-5.png",
            10,
        )
    )
    chick_shop.add_new_product(
        Product(
            12,
            "Fleece Jacket",
            5.99,
            "Accessory",
            "red",
            "img/new-6.png",
            10,
        )
    )

    chick_shop.add_product_to_cart("chicken", 3, 2)
    chick_shop.add_product_to_cart("chicken", 2, 2)
    chick_shop.add_product_to_cart("chicken", 1, 2)
    chick_shop.add_product_to_cart("chicken", 6, 2)
    chick_shop.add_product_to_cart("chicken", 5, 2)
    chick_shop.add_product_to_cart("chicken", 4, 2)


create_new_instances()


######################CHECK LOGIN######################
@app.post("/", response_class=HTMLResponse)
def post_home(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
):

    account = chick_shop.search_account_by_username(username)

    if account and account.password == password:
        template_data = get_template_data(username)
        template_data.update({"request": request})
        response = templates.TemplateResponse("index.html", template_data)
        response.set_cookie("username", account.username)
        return response

    return templates.TemplateResponse(
        "login.html",
        {
            "request": request,
            "error_message": "Login unsuccessful. Please try again.",
        },
    )


######################PAGE LOGIN######################
@app.get("/login", response_class=HTMLResponse)
def get_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


######################CHECK LOGOUT######################
@app.get("/logout", response_class=HTMLResponse)
def logout():
    response = RedirectResponse(url="/")
    response.delete_cookie("username")
    return response


######################PAGE HOME######################
@app.get("/", response_class=HTMLResponse)
def get_index(request: Request, username: str = Cookie(default=None)):
    template_data = get_template_data(username)
    template_data.update({"request": request})
    return templates.TemplateResponse("index.html", template_data)


######################PAGE SHOP######################
@app.get("/shop", response_class=HTMLResponse)
def get_shop(request: Request, username: str = Cookie(default=None)):
    template_data = get_template_data(username)
    template_data.update({"request": request})
    return templates.TemplateResponse("shop.html", template_data)


######################PAGE DETAILS######################
@app.get("/details/{product_id}")
def details(request: Request, product_id: int, username: str = Cookie(default=None)):
    product = chick_shop.search_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    template_data = get_template_data(username)
    template_data.update({"request": request, "product": product})
    return templates.TemplateResponse("details.html", template_data)


######################CHECK OUT ORDER######################
@app.get("/check-out-order", response_class=HTMLResponse)
def get_check_out_order(request: Request, username: str = Cookie(default=None)):
    template_data = get_template_data(username)
    template_data.update({"request": request})
    return templates.TemplateResponse("order.html", template_data)


@app.delete("/remove-product-form-cart/{product_id}")
async def remove_product(
    product_id: int, request: Request, username: str = Cookie(default=None)
):
    cart = chick_shop.show_cart(username)
    try:
        chick_shop.remove_product_from_cart(username, product_id)
        total_price = cart.total_price
        quantity = cart.total_quantity
        return {
            "message": "Product removed successfully",
            "total_price": total_price,
            "quantity": quantity,
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.post("/add-to-cart")
async def add_to_cart(
    product_id: int, quantity: int, username: str = Cookie(default=None)
):
    # print(product_id, quantity)
    chick_shop.add_product_to_cart(username, product_id, quantity)
    return {"message": "Product added to cart successfully"}


def get_template_data(username: str):
    product_list = chick_shop.get_product_list
    account = chick_shop.search_account_by_username(username)
    if account:
        cart = chick_shop.show_cart(username)
        return {
            "username": username,
            "product_list": product_list,
            "cart": cart,
            "account": account,
        }
    return {"product_list": product_list}
