# main.py
from fastapi import FastAPI, Depends, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from models import Account, Product, Controller

app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")
templates = Jinja2Templates(directory="templates")

chick_shop = Controller()
chick_shop.add_account(Account("chicken", "0000"))


def add_new_product():
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


def is_user_logged_in(request: Request):
    return "user" in request.cookies


def is_user_authenticated(username: str = Form(...), password: str = Form(...)):
    account = chick_shop.get_account_by_username(username)
    if account and account.password == password:
        return account
    return None


@app.post("/", response_class=HTMLResponse)
def post_home(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    logged_in: bool = Depends(is_user_logged_in),
    account: Account = Depends(is_user_authenticated),
):
    if account:
        response = templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "user": account.username,
                "products": chick_shop.get_product(),
            },
        )
        response.set_cookie("user", account.username)
        return response
    return templates.TemplateResponse(
        "login.html",
        {
            "request": request,
            "error_message": "Login unsuccessful. Please try again.",
            "products": chick_shop.get_product(),
        },
    )


@app.get("/login", response_class=HTMLResponse)
def get_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/", response_class=HTMLResponse)
def get_home(request: Request, logged_in: bool = Depends(is_user_logged_in)):
    return templates.TemplateResponse(
        "index.html", {"request": request, "products": chick_shop.get_product()}
    )


@app.get("/shop", response_class=HTMLResponse)
def get_shop(request: Request):
    return templates.TemplateResponse(
        "shop.html", {"request": request, "products": chick_shop.get_product()}
    )


@app.get("/index", response_class=HTMLResponse)
def get_index(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "products": chick_shop.get_product()}
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
