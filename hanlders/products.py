import json
import re


def get_product_list(data):

    def filter_by_category(file):
        lst = []
        for cat in file:
            if data['filter']['category'] is None:
                for prod in cat['products']:
                    lst.append(prod)
            if cat['id'] == data['filter']['category']:
                for prod in cat['products']:
                    lst.append(prod)
        return lst

    with open('data/catalog.json') as catalog:
        file_data = catalog.read()
        file = filter_by_category(json.loads(file_data))

        if not file: return {'code': 500, 'data':[]}

        for prod in file.copy():
            try:
                if re.findall(r'[><=]\d+',data['filter']['price']):
                    if not eval(str(prod["price"]) + str(data['filter']['price'])):
                        file.remove(prod)

                else: return {'code': 500, 'data':[]}
            except:
                file

        if not file: return {'code': 200, 'data': []}
        dct = []
        for x in file:
            dct.append(f"{x['id']}. {x['name']} ({x['price']} руб/кг) {x['balance']}шт.")

        return {'code': 200, 'data': '\n'.join(dct)}



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
