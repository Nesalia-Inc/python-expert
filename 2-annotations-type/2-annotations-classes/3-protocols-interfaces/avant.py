import random




        
class Entity:
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
        
        

def random_attack(first : Entity, second : Entity) -> None:
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