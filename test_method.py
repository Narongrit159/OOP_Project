from create_instances import create_new_instances, get_chick_shop_controller

create_new_instances()
chick_shop = get_chick_shop_controller()

# product = chick_shop.search_box_color
# print(product)

# product = chick_shop.search_box_category
# print(product)


# check_box = chick_shop.check_box(["Hoodies"],[])
# for i in check_box:
#     print(i.name,    i.color     ,i.category)

# admin_account = chick_shop.search_account_by_username("admin")
# status_account = chick_shop.check_account_type(admin_account)
# print(status_account)


# check = chick_shop.search_product_by_color("Red")
# for i in check_box:
#     print(i.name,    i.color     ,i.category)

# cart = chick_shop.show_cart("chicken")
# list = cart.show_selected_product_list
# print(list)
# chick_shop.clear_cart("chicken")
# print(list)


order = chick_shop.create_order("chicken",1,1,1)
order2 = chick_shop.create_order("chicken",1,1,1)
order3 = chick_shop.create_order("chicken",1,1,1)
print(order.status)
change1 = chick_shop.change_status_order(1,2)
print(order.status)
change1 = chick_shop.change_status_order(1,3)
print(order.status)
history_order = chick_shop.show_history_order_user("chicken")
print(history_order)