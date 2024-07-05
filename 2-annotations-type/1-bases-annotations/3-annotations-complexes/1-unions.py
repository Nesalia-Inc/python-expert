


class Chien:
    pass 


class Chat:
    pass 



# Il y a des cas où tu veux qu'un paramètre ou une valeur 
# possède plusieurs types de données différents. 
# Lorsque c'est le cas, tu peux utiliser un Union de Type. 
# Tu dois utiliser la syntaxe type1 | type2 | ... | typeN. 

# Cette syntaxe peut être remplacée par l'annotation générique 
# `typing.Union` qui possède la syntaxe :
# `typing.Union[type1, type2, ..., typeN]`
def adopter(animal : Chien | Chat) -> None:
    # Cette fonction accepte donc uniquement les objets 
    # de type `Chien` et `Chat`. Si une opération est uniquement
    # présente dans une des deux classes, le type checker te le diras.
    pass 



if __name__ == '__main__':
    medor = Chien()
    garfield = Chat()
    
    # Cette méthode accepte donc des objets `Chien` et `Chat`. 
    # Si on essaye de mettre des objets d'une autre classe, 
    # une erreur sera renvoyée. 
    adopter(medor)
    adopter(garfield)
    