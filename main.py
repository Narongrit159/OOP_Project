# main.py
from fastapi import FastAPI, HTTPException, Form, Cookie, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from create_instances import create_new_instances, get_chick_shop_controller

app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")
templates = Jinja2Templates(directory="templates")


create_new_instances()
chick_shop = get_chick_shop_controller()


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
    account = chick_shop.search_account_by_username(username)
    payment_method_list = chick_shop.payment_list
    promotion_list = chick_shop.get_promotion_list
    template_data = get_template_data(username)
    address_list = account.address_list

    template_data.update(
        {
            "request": request,
            "address_list": address_list,
            "payment_method_list": payment_method_list,
            "promotion_list": promotion_list,
        }
    )
    return templates.TemplateResponse("order.html", template_data)


@app.post("/submit-order")
async def submit_order(
    request: Request,
    promotion_id: str = Form(...),
    address: str = Form(...),
    pyment_medthod: str = Form(...),
    username: str = Cookie(default=None),
):
    template_data = get_template_data(username)
    template_data.update(
        {
            "request": request,
            "promotion_id": promotion_id,
            "address": address,
            "pyment_medthod": pyment_medthod,
        }
    )
    return templates.TemplateResponse("order_detail.html", template_data)


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
