from create_instances import create_new_instances, get_chick_shop_controller

create_new_instances()
chick_shop = get_chick_shop_controller()

product = chick_shop.search_box_color
print(product)

product = chick_shop.search_box_category
print(product)
