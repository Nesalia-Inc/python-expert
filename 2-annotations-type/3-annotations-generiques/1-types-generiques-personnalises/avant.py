


class Pile:
    def __init__(self, *args) -> None:
        self.__elements = list(args)
        
        
    def push(self, element) -> None:
        self.__elements.append(element)
        
    
    def pop(self):
        if self.est_vide():
            raise ValueError("La pile est vide")
        
        return self.__elements.pop()
    
    def est_vide(self) -> bool:
        return len(self.__elements) == 0
    
    
    
    
if __name__ == "__main__":
    pile = Pile(1, 2, 3)
    
    pile.push("4")
    
    while not pile.est_vide():
        print(pile.pop())
    