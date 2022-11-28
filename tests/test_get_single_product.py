from hanlders.products import get_single_product 
def test1():
    return {
                "action": 4,
                    "data": {
                              "id": 1
                                  }
                }

def test2():
    return {
                "action": 4,
                    "data": {
                              "id": 2
                                  }
                }


def test3():
    return {
                 "action": 4,
                     "data": {
                               "id": None
                                   }
                }
    
def test_get_single_product():
        test_data1 = {'code': 200, 'message': 'Яблоки. Голден.\nЦена: 1000 рублей за кг\nОстаток на складе:10кг\nОписание:Зеленые яблоки, отлично подходят для приготовления пирога'} 
        test_data2 = {'code': 404, 'message': "Товара с таким номером не найдено"}


        assert get_single_product(test1()) == test_data1
        assert get_single_product(test2()) == test_data2
        assert get_single_product(test3()) == test_data2
