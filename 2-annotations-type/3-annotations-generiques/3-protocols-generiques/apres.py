import random
from typing import Generic, Protocol, TypeVar


T = TypeVar("T", contravariant=True)


class CanDie(Protocol):
    def die(self) -> None: ...

class CanAttack(Protocol[T]):
    def attack(self, other : T) -> None: ...
    
    
class Entity(Generic[T], CanAttack[T]):
    def __init__(self, life : int, strengh : int, defense : int) -> None:
        self.life = life 
        self.strengh = strengh
        self.defense = defense
    
    
    def attack(self, other : T) -> None:
        if not isinstance(other, Entity):
            raise ValueError("On peut attaquer uniquement une entité")
        
        other.life -= self.strengh
    
    
    def die(self) -> None:
        print("Je suis mort")
    
    
class Monster(Entity["Player"]):
    pass 


class Player(Entity["Monster"]):
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