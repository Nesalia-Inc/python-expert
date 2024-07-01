


class Range:
    def __init__(self, start: int, end: int, step : int = 1) -> None:
        self.start = start
        self.end = end
        self.step = step

    # La dunder method `__iter__` est appelée lorsqu'on utilises 
    # la fonction `iter()` sur un objet de la classe. Généralement, 
    # on va configurer l'itérateur dans cette méthode. 
    def __iter__(self):
        
        # Comme tu peux le voir ici, on défini la valeur actuelle
        # comme étant le premier élément et on retourne l'instance de la classe. 
        self.current = self.start
        return self

    # La dunder method `__next__` est appelée lorsqu'on utilises
    # la fonction `next()` sur un objet de la classe. Son rôle est de définir
    # quel est l'élément suivant dans l'itérateur. 
    def __next__(self):
        
        # Pour définir que l'on est à la fin de la boucle, on doit 
        # renvoyer une `StopIteration`. Bien que ce soit une erreur, 
        # le programme ne sera pas arrêté. 
        if self.current > self.end or self.current < self.start:
            raise StopIteration
        else:
            current = self.current
            self.current += self.step
            return current


# La boucle `for` appelle automatiquement la méthode `iter`
# puis appelle successivement la méthode `next` jusqu'à avoir
# une `StopIteration`. 
for number in Range(1, 5):
    print(number)  

