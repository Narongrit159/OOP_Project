# main.py
from fastapi import FastAPI, Depends, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models import Account, Product, Controller
from fastapi import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")

chick_shop = Controller()
chick_shop.add_account(Account("chicken", "0000"))

chick_shop.add_product(Product(name="Product 1", price=19))
chick_shop.add_product(Product(name="Product 2", price=28))
chick_shop.add_product(Product(name="Product 3", price=37))
chick_shop.add_product(Product(name="Product 4", price=46))
chick_shop.add_product(Product(name="Product 5", price=55))
chick_shop.add_product(Product(name="Product 6", price=64))
chick_shop.add_product(Product(name="Product 7", price=73))
chick_shop.add_product(Product(name="Product 8", price=82))
chick_shop.add_product(Product(name="Product 9", price=91))


def get_current_user(username: str, password: str):
    if chick_shop.validate_user_credentials(username, password):
        return chick_shop.get_user_by_username(username)
    raise HTTPException(status_code=404, detail="User not found or invalid credentials")


@app.get("/", response_class=HTMLResponse)
def get_home(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
def post_home(request: Request, username: str = Form(...), password: str = Form(...)):
    try:
        user = get_current_user(username, password)
        return templates.TemplateResponse(
            "products.html",
            {
                "request": request,
                "user": user.username,
                "products": chick_shop.get_product(),
            },
        )
    except HTTPException as e:
        return templates.TemplateResponse(
            "login.html", {"request": request, "error_message": str(e.detail)}
        )
