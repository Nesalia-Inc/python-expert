from typing import Callable



def ajouter(condition : Callable[[int, int], bool], a : int, b : int) -> int:
    if condition(a, b):
        return a + b
    raise ValueError