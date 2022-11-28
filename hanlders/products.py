def get_product_list(data):
    pass
import json
def get_single_product(data):
  with open('data/catalog.json') as product_file:
    file_data = json.load(product_file) 
    user_product_id = data['data']['id']
    code = 404
    message = "Товара с таким номером не найдено"
    for category in file_data:
        for product in category['products']:
            if user_product_id == product['id']:
                code = 200
                message = f"{product['name']}\nЦена: {product['price']} рублей за {product['unit']}\nОстаток на складе:{product['balance']}{product['unit']}\nОписание:{product['description']}"
    
    return {'code': code, 'message': message}
