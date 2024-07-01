from typing import Callable, TypeVar
from typing_extensions import ParamSpec

P = ParamSpec('P')
R = TypeVar('R')

def mon_decorateur(f: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print("Avant d'appeler la fonction")
        result = f(*args, **kwargs)
        print("Après avoir appelé la fonction")
        return result
    return wrapper

@mon_decorateur
def add(a: int, b: int) -> int:
    return a + b

print(add(3, 4))
