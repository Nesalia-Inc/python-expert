from typing import TypeVar


T = TypeVar("T", int, float, str)


def ajouter(a : T, b : T) -> T:
    return a + b




if __name__ == '__main__':
    print(ajouter(1, 2))
    print(ajouter("a", "b"))