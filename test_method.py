from create_instances import create_new_instances, get_chick_shop_controller

create_new_instances()
chick_shop = get_chick_shop_controller()

# product = chick_shop.search_box_color
# print(product)

# product = chick_shop.search_box_category
# print(product)


# check_box = chick_shop.check_box(["Hoodies","T-Shirt"],["Red"])
# for i in check_box:
#     print(i.name,    i.color     ,i.category)

admin_account = chick_shop.search_account_by_username("admin")
status_account = chick_shop.check_account_type(admin_account)
print(status_account)