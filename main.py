# main.py
from fastapi import FastAPI, Depends, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models import User, Product, Controller
from fastapi import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Mock data for demonstration purposes
fake_user_db = {
    "chicken": User(username="chicken", password="0000"),
    "user2": User(username="user2", password="pass2"),
}

fake_product_db = {
    "product1": Product(name="Product 1", price=19),
    "product2": Product(name="Product 2", price=28),
    "product3": Product(name="Product 3", price=37),
    "product4": Product(name="Product 4", price=46),
    "product5": Product(name="Product 5", price=55),
    "product6": Product(name="Product 6", price=64),
    "product7": Product(name="Product 7", price=73),
    "product8": Product(name="Product 8", price=82),
    "product9": Product(name="Product 9", price=91),
}


def get_current_user(username: str):
    user = fake_user_db.get(username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get("/", response_class=HTMLResponse)
def get_home(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
def post_home(request: Request, username: str = Form(...)):
    user = fake_user_db.get(username)
    if user is None:
        return templates.TemplateResponse("login.html", {"request": request})

    return templates.TemplateResponse(
        "products.html",
        {"request": request, "user": username, "products": fake_product_db.values()},
    )
