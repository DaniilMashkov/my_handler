import json
data = {
    "action": 2,
    "filter": {
        "price": None,
        "category": 2
    }
}
def get_product_list(data):

    with open('../data/catalog.json') as catalog:
        file_data = catalog.read()
        file = (json.loads(file_data))

        f_price = data['filter']['price']
        f_category = data['filter']['category']
        all_goods = [x['products'] for x in file]

        for cat in file:
            if cat['id'] == f_category:
                if f_price is None:
                    return [print(x) for x in cat['products']]
                elif '>' or '<'  or'=' in f_price:
                    for i in all_goods:
                        for k in i:
                            filter_price = (eval(str(k["price"])+str(f_price)))
                            if filter_price: print(k)

                else:
                    [print(x) for x in cat['products']]





get_product_list(data)

def get_single_product(data):
    pass
