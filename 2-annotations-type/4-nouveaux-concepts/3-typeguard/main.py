from typing import TypeGuard, overload



# Les TypedGuard sont un concept très intéressant et utile
# qui nous permettent de vérifier une annotation. En gros,
# si cette fonction nous renvoie `True`, cela voudra dire
# que la liste mise en paramètre est bien une chaîne de caractères.
def is_str_list(liste : list[object]) -> TypeGuard[list[str]]:
    
    # Pour vérifier qu'une liste est une liste de chaînes de caractères
    # On doit uniquement vérifier que chaque élément est bien une 
    # chaîne de caractères. 
    return all([isinstance(x, str) for x in liste])

def is_int_list(liste : list[object]) -> TypeGuard[list[int]]:
    return all([isinstance(x, int) for x in liste]) 



@overload
def somme(liste : list[int]) -> int: ...
@overload
def somme(liste : list[str]) -> str: ...


def somme(liste):
    
    # Ensuite, il nous suffit uniquement d'appeler 
    # la fonction et l'annotation du paramètre sera
    # modifiée en conséquences. 
    if is_int_list(liste):
        return sum(liste)
    elif is_str_list(liste):
        result = ""
        
        for element in liste:
            result += element 
            
        return result
    
    raise ValueError



if __name__ == '__main__':
    print(somme([1, 2, 3, 4, 5]))
    print(somme(["1", "2", "3", "4", "5"]))
    