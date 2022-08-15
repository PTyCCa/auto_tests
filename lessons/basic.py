"""Напишите тесты для функции get(collection, key, default_value). Эта функция извлекает значение из словаря при условии, что ключ существует. В ином случае возвращается default_value.

>>> from functions import get_function
>>> get = get_function()
>>>
>>> get({"hello": "world" }, "hello")
world
>>> get({ "hello": "world" }, "hello", "kitty")
world
>>> get({}, "hello", "kitty")
kitty
Тесты должны быть построены по такому же принципу, как это описывалось в теории урока: проверка через if и исключение в случае провала теста.

Для хорошего тестирования этой функции понадобится как минимум три теста:

Проверка, что функция возвращает нужное значение по существующему ключу (прямой тест на работоспособность)
Проверка на то, что возвращается значение по умолчанию, если ключа нет
Проверка на то, что возвращается значение по существующему ключу, даже если передано значение по умолчанию (пограничный случай)"""

from functions import get_function

get = get_function()

# BEGIN
if get({"key": "value"}, "key") != "value":
    raise ValueError('Boom!')

if get({}, "key", "default") != "default":
    raise ValueError('Boom!')

if get({"key": "value"}, "key", "default") != "value":
    raise ValueError('Boom!')
# END