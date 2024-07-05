

# La syntaxe générale pour les annotations de type
# est `variable : type = valeur`. Quand on annote 
# une variable avec des types primitifs, on a accès
# à `str, int, float` et `bool`.  

# Une variable possède par défaut une valeur. 
# Le type checker est intelligent et comprends 
# quelles sont les annotations d'une variable 
# et il n'est donc pas nécessaire de les mettre 
# manuellement. 

nom : str = "Jean"
age : int = 45
taille : float = 1.78
majeur : bool = age >= 18


# Il y a aussi une annotation appelée `Any`
# qui vient du module `typing`. Son rôle est 
# de ne définir aucune annotation explicitement. 
# Cette annotation n'est vraiment pas recommandée
# car elle équivalente à ne pas avoir d'annotations.
from typing import Any 

quelconque : Any = 1
quelconque = "abc"