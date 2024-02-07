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

chick_shop.add_product(Product(name="Product 1", price=19))
chick_shop.add_product(Product(name="Product 2", price=28))
chick_shop.add_product(Product(name="Product 3", price=37))
chick_shop.add_product(Product(name="Product 4", price=46))
chick_shop.add_product(Product(name="Product 5", price=55))
chick_shop.add_product(Product(name="Product 6", price=64))
chick_shop.add_product(Product(name="Product 7", price=73))
chick_shop.add_product(Product(name="Product 8", price=82))
chick_shop.add_product(Product(name="Product 9", price=91))


def get_current_user(username: str, password: str, logged_in: bool = Depends()):
    if not logged_in:
        return None
    account = chick_shop.get_account_by_username(username)
    if account and account.password == password:
        return account
    return None


def is_user_logged_in(request: Request):
    return "user" in request.cookies


@app.get("/", response_class=HTMLResponse)
def get_home(request: Request, logged_in: bool = Depends(is_user_logged_in)):
    if not logged_in:
        return templates.TemplateResponse("index.html", {"request": request})
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
def post_home(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    logged_in: bool = Depends(is_user_logged_in),
):
    try:
        account = get_current_user(username, password, logged_in)
        if account:
            response = templates.TemplateResponse(
                "products.html",
                {
                    "request": request,
                    "user": account.username,
                    "products": chick_shop.get_products(),
                },
            )
            response.set_cookie("user", account.username)
            return response
        return templates.TemplateResponse("index.html", {"request": request})
    except HTTPException as e:
        return templates.TemplateResponse(
            "products.html", {"request": request, "error_message": str(e.detail)}
        )


@app.get("/login", response_class=HTMLResponse)
def get_login(request: Request, logged_in: bool = Depends(is_user_logged_in)):
    if not logged_in:
        return templates.TemplateResponse("login.html", {"request": request})
    return HTMLResponse(url="/", status_code=303)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

css_files = [
    "style.css",
    "swiper-bundle.min.css",
    # เพิ่มไฟล์ CSS ต่อไปตามต้องการ
]
