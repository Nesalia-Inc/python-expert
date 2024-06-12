


def get_pairs(nombres : list[int]) -> list[int]:
    pairs : list[int] = []
    
    for nombre in nombres:
        if nombre % 2 == 0:
            pairs.append(nombre)
            
    return pairs



def get_impairs(nombres : list[int]) -> list[int]:
    impairs : list[int] = []
    
    for nombre in nombres:
        if nombre % 2 == 1:
            impairs.append(nombre)
            
    return impairs



def double(nombres : list[int]) -> list[int]:
    doubles : list[int] = []
    
    for nombre in nombres:
        doubles.append(nombre * 2)
        
    return doubles



def somme(nombres : list[int]) -> int:
    resultat = 0
    
    for nombre in nombres:
        resultat += nombre 
        
    return resultat