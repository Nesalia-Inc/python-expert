




def somme(nombres : list[int]) -> int:
    resultat = 0
    
    for nombre in nombres:
        resultat += nombre 
        
    return resultat



def upper(caracteres : list[str]) -> list[str]:
    majuscules : list[str] = []
    
    for caractere in caracteres:
        majuscules.append(caractere.upper())
        
    return majuscules



if __name__ == '__main__':
    liste = [1, 2, 3, 4, 5]
    caracteres = ["a", "b", "c"] 
    
    
    print(somme(liste))
    print(upper(caracteres))