


# Les dictionnaires ont deux parties : leurs clés et leurs valeurs. 
# Il est donc nécessaire d'annoter les deux. La syntaxe générale 
# est `dict[type_clé, type_valeurs]`. Dans cet exemple, toutes 
# les clés sont des chaînes de caractères et les valeurs des entiers. 
ages : dict[str, int] = {"Jean" : 45, "Jeanne" : 54}



def somme(ages : dict[str, int]) -> int:

    # Le type checker est conscient des annotations du dictionnaire
    # mis en paramètre. Il comprend donc que chaque âge est un entier. 
    return sum([age for age in ages.values()])


def ajouter_age(ages : dict[str, int], nouveau_nom : str, nouvel_age : int) -> dict[str, int]:
    nouveaux_ages = ages.copy()
    
    nouveaux_ages[nouveau_nom] = nouvel_age
    
    return nouveaux_ages


if __name__ == '__main__':
    print(somme(ages))
    ages = ajouter_age(ages, "Paul", 36)
    
    print(ages)