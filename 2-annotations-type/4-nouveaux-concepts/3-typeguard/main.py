from typing import TypeGuard, overload



def is_str_list(liste : list) -> TypeGuard[list[str]]:
    return all([isinstance(x, str) for x in liste])



def check(liste : list[int] | list[str]) -> None:
    if is_str_list(liste):
        print("Je suis une liste de chaînes de caractères")
    else:
        print("Je suis une liste d'entiers")
        
        
        

def is_int_list(liste : list) -> TypeGuard[list[int]]:
    return all([isinstance(x, int) for x in liste]) 



@overload
def somme(liste : list[int]) -> int: ...
@overload
def somme(liste : list[str]) -> str: ...


def somme(liste):
    if is_int_list(liste):
        return sum(liste)
    elif is_str_list(liste):
        result = ""
        
        for element in liste:
            result += element 
            
        return result
    
    raise ValueError



somme([1, 2, 3])