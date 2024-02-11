# main.py
from fastapi import FastAPI, Depends, HTTPException, Form, Cookie, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordRequestForm
from typing import Set
from models import Account, Product, Controller

app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")
templates = Jinja2Templates(directory="templates")

chick_shop = Controller()


def add_new_product():
    chick_shop.add_account(Account("chicken", "0000"))
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


add_new_product()


@app.post("/", response_class=HTMLResponse)
def post_home(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
):

    user = chick_shop.search_account_by_username(username)

    if user and user.password == password:
        response = templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "user": user.username,
                "products": chick_shop.get_product_list,
            },
        )
        response.set_cookie("user", user.username)
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
def get_index(request: Request, user: str = Cookie(default=None)):
    if user:
        account = chick_shop.search_account_by_username(user)
        if account:
            return templates.TemplateResponse(
                "index.html",
                {
                    "request": request,
                    "user": account.username,
                    "products": chick_shop.get_product_list,
                },
            )

    return templates.TemplateResponse(
        "index.html", {"request": request, "products": chick_shop.get_product_list}
    )


@app.get("/shop", response_class=HTMLResponse)
def get_shop(request: Request, user: str = Cookie(default=None)):
    if user:
        account = chick_shop.search_account_by_username(user)
        if account:
            return templates.TemplateResponse(
                "shop.html",
                {
                    "request": request,
                    "user": account.username,
                    "products": chick_shop.get_product_list,
                },
            )
    return templates.TemplateResponse(
        "shop.html", {"request": request, "products": chick_shop.get_product_list}
    )


@app.get("/details/{product_id}")
def details(request: Request, product_id: int):
    user = request.cookies.get("user")

    product = chick_shop.search_product_by_id(product_id)
    product_list = chick_shop.get_product_list

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if user:
        account = chick_shop.search_account_by_username(user)
        if account:
            return templates.TemplateResponse(
                "details.html",
                {
                    "request": request,
                    "user": account.username,
                    "product": product,
                    "product_list": product_list,
                },
            )

    return templates.TemplateResponse(
        "details.html",
        {"request": request, "product": product, "product_list": product_list},
    )


@app.get("/login", response_class=HTMLResponse)
def get_login(request: Request):
    return templates.TemplateResponse(
        "login.html", {"request": request, "products": chick_shop.get_product_list}
    )


@app.get("/logout", response_class=HTMLResponse)
def logout(request: Request):

    response = RedirectResponse(url="/")
    response.delete_cookie("user")
    return response
