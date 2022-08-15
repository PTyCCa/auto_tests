"""Напишите тесты для функции without(coll, *values), которая принимает первым параметром список и возвращает его копию, из которой исключены значения, переданные вторым и последующими параметрами.

>>> from functions import get_function
>>> without = get_function()
>>>
>>> without([2, 1, 2, 3, 4], 2, 3)
[1, 4]
>>> without([], 2)
[]"""

from functions import get_function

without = get_function()


# BEGIN
def test_without():
    assert without([], 5) == []
    assert without([1, 2, 4, 5, 4, 7, 4], 4, 2) == [1, 5, 7]

# END