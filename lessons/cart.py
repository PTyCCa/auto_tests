"""Напишите тесты для корзины интернет-магазина. Интерфейс:
make_cart() – создаёт новую корзину (объект).
add_item(good, count) – добавляет в корзину товары и их количество. Товар – это объект, у которого два свойства: name (имя) и price (стоимость).
get_items() – возвращает список товаров в формате [{ good, count }, { good, count }, ...]
get_cost() – возвращает стоимость корзины. Стоимость корзины высчитывается как сумма всех добавленных товаров с учётом их количества.
get_count() – возвращает общее количество товаров в корзине.
>>> cart = make_cart()
>>> cart.add_item({ 'name': 'car', 'price': 3 }, 5)
>>> cart.add_item({ 'name': 'house', 'price': 10 }, 2)
>>> len(cart.get_items())
2
>>> cart.get_cost()
35
>>> cart.add_item({ 'name': 'house', 'price': 10 }, 1)
>>> len(cart.get_items())
3
>>> cart.get_cost()
45"""

from Cart import get_implementations


make_cart = get_implementations()


#BEGIN (write your solution here)
import pytest


@pytest.fixture
def cart():
    cart = make_cart()
    return cart


def test_make_cart(cart):
    cart.add_item({ 'name': 'car', 'price': 3 }, 5)
    cart.add_item({ 'name': 'house', 'price': 10 }, 2)
    assert len(cart.get_items()) == 2
    assert cart.get_cost() == 35
    assert cart.get_count() == 7
#END