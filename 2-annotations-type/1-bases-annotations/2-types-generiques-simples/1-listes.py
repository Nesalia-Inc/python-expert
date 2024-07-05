


# Les listes sont le premier type générique que l'on va voir. 
# Un type générique est un type qui est caractérisé par un autre type. 
# Par exemple, une liste d'entiers n'est pas la même chose qu'une liste
# de chaînes de caractères. La différence est causée par les éléments de 
# cette liste. 

# Quand on annotes une liste, on doit prendre en compte le type de ses éléments. 
# La syntaxe générale pour annoter une liste est `list[type_elements]`. Une liste 
# d'entiers aura donc l'annotation `list[int]`. 


def somme(nombres : list[int]) -> int:
    resultat = 0
    
    # On a défini que `nombres` est une liste d'entiers.
    # Le type checker comprends donc que chaque élément
    # de cette liste est un entier. Cela veut aussi dire
    # que si tu cherches à ajouter des éléments dans cette 
    # liste, tu ne pourras que ajouter des entiers.
    for nombre in nombres:
        resultat += nombre 
        
    return resultat



def upper(caracteres : list[str]) -> list[str]:
    
    # Il est obligatoire de définir les annotations de type
    # d'une liste qui est vide. La raison est que le type checker
    # ne peut pas prédire les types de ses éléments s'il n'en 
    # possède pas. Tu dois donc le définir manuellement
    majuscules : list[str] = []
    
    for caractere in caracteres:
        majuscules.append(caractere.upper())
        
    return majuscules



if __name__ == '__main__':
    
    # Quand une liste possède des éléments, le type checker
    # comprends automatiquement son annotation et il n'est donc
    # pas nécessaire de la préciser manuellement. 
    liste = [1, 2, 3, 4, 5]
    caracteres = ["a", "b", "c"] 
    
    
    print(somme(liste))
    print(upper(caracteres))