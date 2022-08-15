"""Напишите тесты для функции set(coll, path, value) возвращающей словарь, в котором она изменяет (или добавляет) значение по указанному пути. Функция мутирует словарь.

>>> coll = { "a": { "b": { "c": 3 } } }
>>> set(coll, ["a", "b", "c"], 4)
>>> coll["a"]["b"]["c"]
4

>>> set(coll, ['x', 'y', 'z'], 5)
>>> coll['x']['y']['z']
5
Подсказки
Переиспользуйте объект данных
Тесты не должны зависеть друг от друга
Помните о том, что не верная реализация функции set() может возвращать словарь с неправильной структурой"""

import copy

from functions import get_function

set_ = get_function()


# BEGIN
def test_plain_set():
    # TODO: use parametrizing tests
    data = {"a": {"b": {"c": "d"}}}
    data_copy = copy.deepcopy(data)
    set_(data, ['a'], 'value')

    data_copy['a'] = 'value'
    assert data_copy == data


def test_nested_set():
    data = {"a": {"b": {"c": "d"}}}
    data_copy = copy.deepcopy(data)
    set_(data, ['a', 'b', 'c'], 'value')
    data_copy['a']['b']['c'] = 'value'
    assert data_copy == data


def test_new_property_set():
    data = {"a": {"b": {"c": "d"}}}
    data_copy = copy.deepcopy(data)
    set_(data, ['a', 'b', 'd'], 'value')
    data_copy['a']['b']['d'] = 'value'
    assert data_copy == data
# END