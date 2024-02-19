from create_instances import create_new_instances, get_chick_shop_controller

create_new_instances()
chick_shop = get_chick_shop_controller()

product = chick_shop.search_product_by_id(1)
print(product.name)
