import random
from typing import Protocol


# Les protocols sont un moyen de définir des interfaces
# qui possèdent uniquement les comportements que l'on souhaite. 
# Contrairement aux classes abstraites, les protocols sont utilisés
# pour définir des comportements. Les classes abstraites représentent 
# des données abstraites tel qu'un Animal.
class CanDie(Protocol):
    def die(self) -> None: ...
    
    
class CanAttack(Protocol):
    def attack(self, other) -> None: ...
    
    
    
    
# Il est malgré tout possible de faire un héritage entre un Protocol 
# et une classe. Ca nous obligera à créer les méthodes et les attributs qui 
# se trouvent dans le protocol. Une erreur sera renvoyée au moment de la création
# de l'objet s'il ne respecte pas le protocol. 
class Entity(CanDie):
    def __init__(self, life : int, strengh : int, defense : int) -> None:
        self.life = life 
        self.strengh = strengh
        self.defense = defense
    
    
    def attack(self, other) -> None:
        if not isinstance(other, Entity):
            raise ValueError
        
        other.life -= self.strengh
    
    
    def die(self) -> None:
        print("Je suis mort")
    
    
class Monster(Entity):
    pass 


class Player(Entity):
    pass 
        
        
# Les protocols utilisent ce que l'on appelle un typage structurel. 
# Ca veut donc dire qu'ils vont regarder si le paramètre possède ce qu'on 
# lui demande (dans ce cas, une fonction attack) au moment de l'appel 
# de la fonction. 
def random_attack(first : CanAttack, second : CanAttack) -> None:
    choice = random.choice([first, second])
    
    if choice == first:
        choice.attack(second)
    else:
        choice.attack(first)
        
        
if __name__ == '__main__':
    player = Player(100, 25, 10)
    monster = Monster(50, 10, 5)
    
    random_attack(player, monster)
    
    print(player.life, monster.life)