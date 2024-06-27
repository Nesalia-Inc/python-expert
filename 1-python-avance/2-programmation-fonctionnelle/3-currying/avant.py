from functools import partial



def ajouter(a : int, b : int) -> int:
    return a + b 


ajouter_3 = partial(ajouter, 3)
print(ajouter_3())

print(ajouter(1, 2))



# from typing import Callable


# def ajouter(a : int) -> Callable[[int], int]:
#     def ajouter_b(b : int) -> int:
#         return a + b 
#     return ajouter_b



# ajouter_3 = ajouter(3) 

# print(ajouter_3())
