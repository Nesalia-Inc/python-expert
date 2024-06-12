




def get_indice_valeur(prenoms : list[str], prenom_recherche : str) -> int:
    for indice, prenom in enumerate(prenoms):
        if prenom == prenom_recherche:
            return indice
        
    raise ValueError



def get_indice_valeur_base(prenoms : list[str], prenom_recherche : str) -> int:
    indice = 0
    for prenom in prenoms:
        if prenom == prenom_recherche:
            return indice
        indice += 1
        
    raise ValueError


def ajout_multiple(nombres1 : list[int], nombres2 : list[int]) -> list[int]:
    nouveaux_nombres : list[int] = []
    
    for nombre1, nombre2 in zip(nombres1, nombres2):
        nouveaux_nombres.append(nombre1 + nombre2)

    return nouveaux_nombres


def generer_liste(taille : int) -> list[int]:
    return [i for i in range(taille)] 


def get_nombres_pairs(nombres : list[int]) -> list[int]:
    return [nombre for nombre in nombres if nombre % 2 == 0]



if __name__ == '__main__':
    nombres = list(range(10))
    nombres2 = list(range(10))
    
    print(ajout_multiple(nombres, nombres2))
    