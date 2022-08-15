"""Напишите тесты для функции take(items, n), которая возвращает первые n элементов из списка:

>>> take([], 2)
[]
>>> take([1, 2, 3])
[1]
>>> take([1, 2, 3], 2)
[1, 2]
>>> take([4, 3], 9)
[4, 3]"""

from functions import get_function

take = get_function()

#BEGIN
assert take(['one', 'two', 8], 9) == ['one', 'two', 8]
assert take([1, 2]) == [1]
assert take(['one', 'two', 'three'], 2) == ['one', 'two']
assert take(['one', 'two', 'three'], 0) == []
assert take([]) == []
#END