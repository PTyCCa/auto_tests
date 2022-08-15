import os

import right
import wrong1
import wrong2
import wrong3

functions = {
    "right": {
        "get": right.get,
        "index_of": right.index_of,
        "slice": right.my_slice,
    },
    "wrong1": {
        "get": wrong1.get,
        "index_of": wrong1.index_of,
        "slice": wrong1.my_slice,
    },
    "wrong2": {
        "get": wrong2.get,
        "index_of": wrong2.index_of,
        "slice": wrong2.my_slice,
    },
    "wrong3": {
        "get": wrong3.get,
        "index_of": wrong3.index_of,
        "slice": wrong3.my_slice,
    },
}


def get_functions():
    name = os.environ["FUNCTION_VERSION"]
    return functions[name]

def get(coll, index, default=None):

    if (index >= len(coll) or index < 0):
        if default is not None:
            return default
        return None

    return coll[index]

def index_of(coll, value, from_index=0):
    length = len(coll)

    if length == 0:
        return -1

    index = from_index

    if index < 0:
        if index < -length:
            index = 0
        else:
            index += length

    try:
        return coll.index(value, index)
    except ValueError:
        return -1

def my_slice(coll, start=0, end=None):
  length = len(coll)

  normalized_end = length if end is None else end

  if length == 0:
      return []

  normalized_start = start

  if normalized_start < 0:
      if normalized_start < -length:
          normalized_start = 0
      else:
          normalized_start += length

  return coll[normalized_start:normalized_end]



