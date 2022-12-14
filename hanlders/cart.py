import json


def put_product_to_cart(data):

    pass


def get_cart(data):
    with open('../data/cart.json', encoding='uft-8') as file:
        cart = json.load(file)

    code = 200
    message = ""
    for i in cart:
        message += (f"{i['id']}. {i['name']} ({i['price']}) добавлено {i['count']} штук \n")

    return {
        "code": code,
        "message": message
    }

    with open('data/catalog.json', 'r', encoding='utf-8') as catalog:
        catalog_data = json.load(catalog)

    chosen_product = None

    for category in catalog_data:
        for product in category['products']:
            if product['id'] == data['data']['id']:
                chosen_product = product

    if chosen_product is None:
        return {
            "code": 404,
            "message": "Товара с таким номер не найдено."
        }

    else:
        product_id = chosen_product['id']
        product_name = chosen_product['name']
        product_price = str(chosen_product['price']) + 'руб./' + chosen_product['unit']
        product_unit = chosen_product['unit']
        product_count = data['data']['count']

        if product_count > chosen_product['balance']:
            return {
                "code": 409,
                "message": f"Невозможно добавить товар {product_name} в количестве {product_count} {product_unit} в корзину, потому что их осталось всего {chosen_product['balance']}."
            }

        else:
            to_cart = [{
                'id': product_id,
                'name': product_name,
                'price': product_price,
                'count': product_count,
            }]

            cart_list = []

            with open('data/cart.json', 'r', encoding='utf-8') as cart_r:
                cart_data = json.load(cart_r)
                for product_in_cart in cart_data:
                    cart_list.append(product_in_cart)
                cart_list.append(to_cart[0])
                with open('data/cart.json', 'w', encoding='utf-8') as cart_w:
                    json.dump(cart_list, cart_w, ensure_ascii=False)

            return {
                "code": 201,
                "message": f"Товар {product_name} в количестве {product_count} {product_unit} добавлен в корзину успешно"
            }

