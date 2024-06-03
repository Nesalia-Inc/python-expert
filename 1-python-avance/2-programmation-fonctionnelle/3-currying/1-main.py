from typing import Callable


def ajouter(a : int) -> Callable[[int], int]:
    def ajouter_b(b : int) -> int:
        return a + b 
    return ajouter_b


if __name__ == '__main__':
    ajouter_3 = ajouter(3)
    
    print(ajouter_3(5))