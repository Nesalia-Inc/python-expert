from functools import reduce


def get_pairs(nombres : list[int]) -> list[int]:
    return list(filter(lambda x: x % 2 == 0, nombres))


def get_impairs(nombres : list[int]) -> list[int]:
    return list(filter(lambda x: x % 2 == 1, nombres))


def double(nombres : list[int]) -> list[int]:
    return list(map(lambda x: x * 2, nombres))


def somme(nombres : list[int]) -> list[int]:
    return reduce(lambda x, y : x + y, nombres) # type: ignore



print(somme([1, 2, 3, 4, 5]))