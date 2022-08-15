"""В этом упражнении вам предстоит попрактиковаться в подходе "Разработка через тестирование". Вам нужно будет написать и тесты и реализацию функции. Сначала напишите тесты и запуcтите тестирование. Тесты должны упасть. Затем напишите решение, которое будет проходить тесты.

tests/test_fill.py
Напишите тесты для функции fill(coll, value, begin, end), которая заполняет элементы списка переданным значением, начиная со старта и заканчивая (но не включая) конечной позицией. Функция меняет исходный список!

Функция принимает следующие аргументы:

coll – список, элементы которого будут заполнены
value – значение, которым будут заполнены элементы списка
begin – стартовая позиция, по умолчанию равна нулю
end – конечная позиция, по умолчанию равна длинне списка
# все вызовы нужно рассматривать, как независимые
coll =  [1, 2, 3, 4]

fill(coll, '*', 1, 3)
print(coll)  # => [1, '*', '*', 4]

fill(coll, '*')
print(coll)  # => ['*', '*', '*', '*']

fill(coll, '*', 4)
print(coll)  # => [1, 2, 3, 4]

fill(coll, '*', 0, 10)
print(coll)  # => ['*', '*', '*', '*']
src/solution.py
Реализуйте функцию fill(coll, value, begin, end), основываясь на описании и примерах её работы."""

# BEGIN
def fill(coll, value, begin=0, end=None):
    chunk = [value for _ in coll[begin:end]]
    coll[begin:end] = chunk
# END

import os

import pytest

import right
import solution
import wrong1
import wrong2
import wrong3


@pytest.fixture(name='fill')
def _fill():
    name = os.environ['FUNCTION_VERSION']
    return {
        "user_implementation": solution,
        "right": right,
        "wrong1": wrong1,
        "wrong2": wrong2,
        "wrong3": wrong3,
    }[name].fill


@pytest.fixture(name='collection')
def _collection():
    return [1, 2, 3, 4]


def test_fill(collection, fill):
    fill(collection, '*', 1, 3)
    assert collection == [1, '*', '*', 4]


# BEGIN
def test_fill_default(collection, fill):
    fill(collection, '*')
    assert collection == ['*', '*', '*', '*']


def test_fill_start_ge_length(collection, fill):
    fill(collection, '*', 10, 12)
    assert collection == [1, 2, 3, 4]


def test_fill_start_ge_end(collection, fill):
    fill(collection, '*', 2, 2)
    assert collection == [1, 2, 3, 4]


def test_fill_end_ge_length(collection, fill):
    fill(collection, '*', 0, 10)
    assert collection == ['*', '*', '*', '*']
# END