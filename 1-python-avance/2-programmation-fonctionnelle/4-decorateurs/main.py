from functools import wraps
from typing import Callable


# Un décorateur est une fonction qui prends en paramètre 
# une autre fonction, qui va ajouter un comportement quelconque
# à cette fonction puis va l'appeler à nouveau. 

# Cette fonction prends en paramètre une fonction quelconque
# et l'ensemble des paramètres de cette fonction. Son rôle
# est d'afficher un message pour dire que la fonction a été
# appelée puis appeler la fonction. 
def logging(func : Callable, *args, **kwargs):
    print("Log : Fonction appelée")
    return func(*args, **kwargs)


# Il existe une syntaxe précise avec les décorateurs
# en python qui nous "force" à utiliser une syntaxe 
# précise. On va commencer par créer une fonction
# qui va prendre en paramètre une autre fonction. 
# Le nom de cette fonction sera le nom du décorateur.
# Elle va aussi renvoyer une autre fonction.
def decorateur_logging(func : Callable) -> Callable:
    # Le décorateur `@wraps` est simplement utilisée
    # car les décorateurs ont tendance à supprimer les
    # annotations de type et la documentation des fonctions
    # qu'elles décorent. Son rôle est de supprimer ce comportement
    @wraps(func)
    def wrapper(*args, **kwargs):
        # On va ensuite définir une fonction interne qui 
        # va prendre en paramètre tous les paramètres de 
        # la fonction `func`. Cette fonction est ce que 
        # l'on appelle un "wrapper" est c'est elle qui 
        # va ajouter le comportement que l'on veut. 
        print("Log : Fonction appelée")
        
        # Une fois que le comportement est ajouté, 
        # elle va appeler `func` avec tous ses paramètres
        return func(*args, **kwargs)
    
    # On termine le décorateur en retournant le wrapper
    return wrapper


def logging_personnalise(message : str) -> Callable[[Callable], Callable]:
    def decorateur(func : Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(message)
            func(*args, **kwargs)
        return wrapper 
    return decorateur
            
            
            
# On utilise un décorateur avec la syntaxe
# `@decorateur` au dessus de la fonction
# que l'on veut décorer.
@decorateur_logging
@logging_personnalise("Je suis un test")
def ajouter(a : int, b : int) -> int:
    return a + b 



if __name__ == '__main__':
    logging(ajouter, 1, 2)
    
    