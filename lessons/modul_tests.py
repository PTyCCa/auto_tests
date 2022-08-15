"""Напишите тесты для валидатора, который проверяет корректность данных. Принцип работы валидатора следующий:

С помощью метода add_check(fn) в него добавляются проверки. Каждая проверка представляет из себя функцию-предикат, которая принимает на вход проверяемое значение и возвращает либо True либо False в зависимости от того, соответствует ли значение требованиям проверки или нет.
С помощью метода is_valid(value), пользователь проверяет соответствие значения всем добавленным проверкам. Если не было добавлено ни одной проверки, считается, что любое значение верное.
>>> from validators import get_validator
>>> make_validator = get_validator()
>>> add_check, is_valid = make_validator()
>>> is_valid("some value")
True
>>> add_check(lambda x : x > 5)
>>> add_check(lambda x : x % 2 == 0)
>>> is_valid(3)
False
>>> is_valid(4)
False
>>> is_valid(7)
False
>>> is_valid(8)
True
>>>"""

from validators import get_validator

# Такие штуки правильно делать через фикстуры.
# В следущих уроках мы разберём это подробнее.
make_validator = get_validator()


def test_validator():
    add_check, is_valid = make_validator()
    assert is_valid("value")
# BEGIN
    add_check(lambda x: isinstance(x, int))
    assert not is_valid("value")
    assert is_valid(5)

    add_check(lambda x: x > 10)
    add_check(lambda x: x % 2 == 0)
    assert not is_valid(8)
    assert not is_valid(21)
    assert is_valid(12)
# END