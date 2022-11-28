from hanlders.products import get_product_list


def command ():
  return {
    "action": 2,
    "filter": {
        "price": None,
        "category": None
    }
}

def command1 ():
  return {
    "action": 2,
    "filter": {
        "price": '>=80',
        "category": None
    }
}

def command2 ():
  return {
    "action": 2,
    "filter": {
        "price": None,
        "category": 1
    }
}

def command3 ():
  return {
    "action": 2,
    "filter": {
        "price": 'AVnfa',
        "category": 2
    }
}

def command4 ():
  return {
    "action": 2,
    "filter": {
        "price": '<9999',
        "category": 4
    }
}

def test_get_product_list():
    test_data = {
        'code': 200,
        'data': '1. Яблоки. Голден. (1000 руб/кг) 10шт.\n2. Груши. Хуюши. (8 руб/кг) 400шт.\n'
                '1. Лук (50 руб/кг) 200шт.\n2. Морковь (80 руб/кг) 300шт.'
    }
    assert get_product_list(command()) == test_data

def test_get_product_list1():
    test_data = {
        'code': 200,
        'data': '1. Яблоки. Голден. (1000 руб/кг) 10шт.\n2. Морковь (80 руб/кг) 300шт.'
    }
    assert get_product_list(command1()) == test_data


def test_get_product_list2():
    test_data = {
        'code': 200,
        'data': '1. Яблоки. Голден. (1000 руб/кг) 10шт.\n2. Груши. Хуюши. (8 руб/кг) 400шт.'
    }
    assert get_product_list(command2()) == test_data


def test_get_product_list3():
    test_data = {'code': 500, 'data': []}

    assert get_product_list(command3()) == test_data


def test_get_product_list4():
    test_data = {'code': 500, 'data': []}
    assert get_product_list(command4()) == test_data