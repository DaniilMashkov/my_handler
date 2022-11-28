from hanlders.products import get_product_list



command = {
    "action": 2,
    "data": {
        "price": None,
        "category": None
    }
}

command1 = {
    "action": 2,
    "data": {
        "price": '>=90',
        "category": None
    }
}

command2 ={
    "action": 2,
    "data": {
        "price": None,
        "category": 1
    }
}

command3 = {
    "action": 2,
    "data": {
        "price": 'AVnfa',
        "category": 2
    }
}

command4 = {
    "action": 2,
    "data": {
        "price": '<9999',
        "category": 4
    }
}

def test_get_product_list():
    test_data = {
        'code': 200,
        'data': '1. Яблоки. Голден. (1000 руб/кг) 10шт.\n2. Груши (200 руб/кг) 30шт.\n'
                '3. Лук. Репчатый (80 руб/кг) 100шт.\n4. Морковь (90 руб/кг) 200шт.'}

    assert get_product_list(command) == test_data

def test_get_product_list1():
    test_data = {
        'code': 200,
        'data': '1. Яблоки. Голден. (1000 руб/кг) 10шт.\n2. Груши (200 руб/кг) 30шт.\n4. Морковь (90 руб/кг) 200шт.'
    }
    assert get_product_list(command1) == test_data


def test_get_product_list2():
    test_data = {
        'code': 200,
        'data': '1. Яблоки. Голден. (1000 руб/кг) 10шт.\n2. Груши (200 руб/кг) 30шт.'
    }
    assert get_product_list(command2) == test_data


def test_get_product_list3():
    test_data = {'code': 500, 'data': []}

    assert get_product_list(command3) == test_data


def test_get_product_list4():
    test_data = {'code': 500, 'data': []}
    assert get_product_list(command4) == test_data