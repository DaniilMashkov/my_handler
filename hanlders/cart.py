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
