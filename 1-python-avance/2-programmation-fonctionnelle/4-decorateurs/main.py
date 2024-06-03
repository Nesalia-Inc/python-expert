from functools import wraps
from typing import Callable


def logging(func : Callable, *args, **kwargs):
    print("Log : Fonction appelée")
    return func(*args, **kwargs)


def decorateur_logging(func : Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Log : Fonction appelée")
        return func(*args, **kwargs)
    return wrapper


def logging_personnalise(message : str) -> Callable[[Callable], Callable]:
    def decorateur(func : Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(message)
            func(*args, **kwargs)
        return wrapper 
    return decorateur
            
            
            
@logging
@logging_personnalise("Je suis un test")
def ajouter(a : int, b : int) -> int:
    return a + b 



if __name__ == '__main__':
    logging(ajouter, 1, 2)
    
    