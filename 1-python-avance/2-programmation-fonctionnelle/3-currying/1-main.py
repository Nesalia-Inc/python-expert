from typing import Callable


# Le currying est un concept qui nous permet de faire 
# des opérations en plusieurs étapes. Ici, au lieu de 
# faire a + b directement, on a la possibilité de définir
# la valeur de `a` d'abord puis de l'ajouter à n'importe 
# quelle valeur `b`. 
def ajouter(a : int) -> Callable[[int], int]:
    
    # Le currying fonction avec des fonctions internes.
    # Celle-ci prends en paramètre la seconde valeur de l'addition
    # et fait l'addition entre les deux valeurs. 
    def ajouter_b(b : int) -> int:
        return a + b 
    
    # Pour que le code fonctionne, on doit retourner 
    # la fonction interne. En gros, la fonction générale
    # va être utilisée comme fonction intermédiaire que
    # l'on pourra appeler une seconde fois pour l'addition
    return ajouter_b


if __name__ == '__main__':
    # On commence par définir la valeur de `a`
    ajouter_3 = ajouter(3)
    
    # On peut ensuite appeler cette fonction encore et encore
    print(ajouter_3(5))
    print(ajouter_3(7))
    
    # Il est donc aussi possible d'appeler directement 
    # les deux fonctions au même moment. 
    print(ajouter(2)(6))