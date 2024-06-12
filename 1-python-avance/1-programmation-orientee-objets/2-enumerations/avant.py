from enum import Enum, auto  


class Status(Enum):
    OPEN = auto()
    IN_PROGRESS = auto()
    CLOSED = auto() 
    
    
    @classmethod
    def next(cls, current : "Status") -> "Status":
        all_status = list(Status) 
        index = all_status.index(current)
        
        return all_status[(index + 1) % 3]
    
    
class Priority(Enum):
    LOW = auto()
    MEDIUM = auto()
    URGENT = auto()
    
    NORMAL = LOW 
    IMPORTANT = MEDIUM
    HIGH = URGENT
    

  

class Ticket:
    def __init__(self, title : str, description : str, priority : Priority):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = Status.OPEN
    
    def __str__(self) -> str:
        return f"Ticket(title={self.title}, description={self.description}, priority={self.priority}, status={self.status})"
    




if __name__ == "__main__":
    ticket = Ticket("Bug dans le système de connection", "Le client ne peut pas se connecter", Priority.NORMAL) 
    
    ticket.status = Status.next(Status.IN_PROGRESS)
    
    print(ticket)
