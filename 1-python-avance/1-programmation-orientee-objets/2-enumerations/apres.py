from enum import Enum, auto 


class Status(Enum):
    OPEN = auto()
    IN_PROGRESS = auto()
    CLOSED = auto()
    
    @classmethod
    def next(cls, current : "Status") -> "Status":
        all_status = list(cls)
        index = all_status.index(current)
        
        return all_status[(index + 1) % 3]
    
    
class Priority(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()

    NORMAL = LOW    
    IMPORTANT = MEDIUM
    URGENT = HIGH
    
    
    
class Ticket:
    def __init__(self, title : str, description : str, priority : Priority):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = Status.OPEN
    
    def __str__(self) -> str:
        return f"Ticket(title={self.title}, description={self.description}, priority={self.priority.name}, status={self.status.name})"
    
    def update_status(self, new_status : Status) -> None:
        if not isinstance(new_status, Status):
            raise ValueError("Invalid status value")
        self.status = new_status
    
    def update_priority(self, new_priority : Priority) -> None:
        if not isinstance(new_priority, Priority):
            raise ValueError("Invalid priority value")
        self.priority = new_priority



if __name__ == "__main__":
    ticket = Ticket("Bug dans le système de connection", "Le client ne peut se connecter", Priority.HIGH) 
    
    ticket.update_status(Status.next(ticket.status)) 
    
    print(ticket)
    