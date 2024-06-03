from functools import partial



def ajouter(a : int, b : int) -> int:
    return a + b 



if __name__ == '__main__':
    ajouter_3 = partial(ajouter, 3)
    
    print(ajouter_3(5))