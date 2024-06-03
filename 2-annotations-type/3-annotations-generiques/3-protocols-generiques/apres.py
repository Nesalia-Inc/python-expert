import random
from typing import Protocol, TypeVar


T = TypeVar("T", contravariant=True)


class CanDie(Protocol):
    def die(self) -> None: ...
    
    
class CanAttack(Protocol[T]):
    def attack(self, other : T) -> None: ...
    
    
    
    
class Entity(CanDie, CanAttack["Entity"]):
    def __init__(self, life : int, strengh : int, defense : int) -> None:
        self.life = life 
        self.strengh = strengh
        self.defense = defense
    
    
    def attack(self, other : "Entity") -> None:
        other.life -= self.strengh
    
    
    def die(self) -> None:
        print("Je suis mort")
    
    
class Monster(Entity):
    pass 


class Player(Entity):
    pass 
        
        

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