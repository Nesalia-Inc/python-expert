from typing import Callable

from functools import wraps



def logging(message : str) -> Callable[[Callable], Callable]:
    def decorateur(func : Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(message)
            return func(*args, **kwargs)
        
        return wrapper
    return decorateur
    


@logging("Deux nombres ont été ajoutés")
def ajouter(a : int, b : int) -> int:
    """Ajoute deux nombres"""
    return a + b 



print(ajouter(1, 2))
