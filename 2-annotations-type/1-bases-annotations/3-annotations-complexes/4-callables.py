from typing import Callable


def ajouter(a : int, b : int) -> int:
    return a + b 

# Chaque fonction possède elle aussi une annotation de type. 
# Elles sont ce que l'on appelle un callable. Pour les annoter,
# on peut donc utiliser l'annotation `Callable`. Sa syntaxe
# est la suivante :
# `Callable[[type_param_1, ..., type_param_N], type_retour]`
# Le premier élément est la liste des types de ses paramètres 
# et le second est le type de retour de la fonction. 

# La fonction ajouter a deux entiers en paramètres et retourne
# un autre entier. On se retrouve donc avec cette annotation. 
fonction : Callable[[int, int], int] = ajouter


# Il est aussi possible de mettre des `Callable` en paramètre pour créer des fonctions
# plus modulaires. Ici, on accepte toutes les fonctions qui prennent en paramètre deux
# entiers et retournent un booléen. Toutes les autres fonctions sont refusées. 
def ajouter_condition(condition : Callable[[int, int], bool], a : int, b : int) -> int:
    if condition(a, b):
        return a + b
    raise ValueError


if __name__ == '__main__':
    print(ajouter_condition(lambda x, y : x < y, 1, 5))
