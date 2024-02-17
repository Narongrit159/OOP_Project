# main.py
from fastapi import FastAPI, Depends, HTTPException, Form, Cookie, status, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from models import Account, Product, Controller, Custumer_account, Owner_account, Cart

app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")
templates = Jinja2Templates(directory="templates")

chick_shop = Controller()


def add_new_product():
    chicken_account = Custumer_account(
        "CHICKEN", "0620538988", "chicken", "0000", cart=Cart()
    )
    tar_account = Custumer_account("TAR", "0620538988", "tar", "0000", cart=Cart())
    maysa_account = Custumer_account(
        "MAYSA", "0620538988", "maysa", "0000", cart=Cart()
    )
    admin_account = Owner_account("ADMIN", "0", "admin", "0000", "0278645215")

    chick_shop.add_account(chicken_account)
    chick_shop.add_account(tar_account)
    chick_shop.add_account(maysa_account)
    chick_shop.add_account(admin_account)

    chick_shop.add_product(
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
    chick_shop.add_product(
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

    chick_shop.add_product(
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
    chick_shop.add_product(
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
    chick_shop.add_product(
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
    chick_shop.add_product(
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

    chick_shop.add_product(
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
    chick_shop.add_product(
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

    chick_shop.add_product(
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
    chick_shop.add_product(
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
    chick_shop.add_product(
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
    chick_shop.add_product(
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


add_new_product()


@app.post("/", response_class=HTMLResponse)
def post_home(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
):

    account = chick_shop.search_account_by_username(username)

    if account and account.password == password:
        response = templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "username": account.username,
                "products": chick_shop.get_product_list,
                "cart": chick_shop.show_cart(username),
            },
        )
        response.set_cookie("username", account.username)
        return response
    else:
        return templates.TemplateResponse(
            "login.html",
            {
                "request": request,
                "error_message": "Login unsuccessful. Please try again.",
            },
        )


@app.get("/", response_class=HTMLResponse)
def get_index(request: Request, username: str = Cookie(default=None)):
    if username:
        account = chick_shop.search_account_by_username(username)
        if account:
            return templates.TemplateResponse(
                "index.html",
                {
                    "request": request,
                    "username": account.username,
                    "products": chick_shop.get_product_list,
                    "cart": chick_shop.show_cart(username),
                },
            )

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "products": chick_shop.get_product_list},
    )


@app.get("/shop", response_class=HTMLResponse)
def get_shop(request: Request, username: str = Cookie(default=None)):
    if username:
        account = chick_shop.search_account_by_username(username)
        if account:
            return templates.TemplateResponse(
                "shop.html",
                {
                    "request": request,
                    "username": account.username,
                    "products": chick_shop.get_product_list,
                    "cart": chick_shop.show_cart(username),
                },
            )
    return templates.TemplateResponse(
        "shop.html",
        {"request": request, "products": chick_shop.get_product_list},
    )


@app.get("/details/{product_id}")
def details(request: Request, product_id: int):

    username = request.cookies.get("username")
    product = chick_shop.search_product_by_id(product_id)
    product_list = chick_shop.get_product_list

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if username:
        account = chick_shop.search_account_by_username(username)
        if account:
            return templates.TemplateResponse(
                "details.html",
                {
                    "request": request,
                    "username": account.username,
                    "product": product,
                    "product_list": product_list,
                    "cart": chick_shop.show_cart(username),
                },
            )

    return templates.TemplateResponse(
        "details.html",
        {
            "request": request,
            "product": product,
            "product_list": product_list,
        },
    )


@app.get("/login", response_class=HTMLResponse)
def get_login(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request, "products": chick_shop.get_product_list},
    )


@app.get("/logout", response_class=HTMLResponse)
def logout(request: Request):

    response = RedirectResponse(url="/")
    response.delete_cookie("username")
    return response


@app.delete("/remove-product/{product_id}")
async def remove_product(product_id: int, request: Request):
    username = request.cookies.get("username")
    try:
        chick_shop.remove_product_from_cart(username, product_id)
        return {"message": "Product removed successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.post("/add-to-cart/{product_id}")
async def add_to_cart(product_id: int, quantity: int):
    print(product_id, quantity)
    return {"message": "Product added to cart successfully"}
