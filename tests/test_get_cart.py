from hanlders.cart import get_cart
from main import main

expected_result = {
    "code": 200,
    "message": "1. Яблоки (200 руб/кг) добавлено 5 штук\n2. Груши (150 руб/кг) добавлено 1 штука"
}

def test_get_cart_func():
    result = get_cart()

    assert result.get('code') == expected_result.get('code')
    assert result.get('message') == expected_result.get('message')


def test_get_cart_main():
    result = main({"action": 6})

    assert result.get('code') == expected_result.get('code')
    assert result.get('message') == expected_result.get('message')