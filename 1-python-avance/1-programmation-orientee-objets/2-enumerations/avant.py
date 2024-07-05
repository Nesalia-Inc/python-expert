
  

class Ticket:
    def __init__(self, title : str, description : str, priority : str):
        self.title = title
        self.description = description
        self.priority = priority
        
        self.status = "OPEN"
    
    def update_status(self, new_status : str) -> None:
        if not new_status in ["OPEN", "IN_PROGRESS", "CLOSED"]:
            raise ValueError("Invalid status value")
        self.status = new_status
    
    def update_priority(self, new_priority : str) -> None:
        if not new_priority in ["LOW", "MEDIUM", "URGENT"]:
            raise ValueError("Invalid priority value")
        self.priority = new_priority
    
        
    def __str__(self) -> str:
        return f"Ticket(title={self.title}, description={self.description}, priority={self.priority}, status={self.status})"
    



if __name__ == "__main__":
    ticket = Ticket("Bug dans le système de connection",
                    "Le client ne peut pas se connecter",
                    "LOW") 
    
    ticket.update_status("IN_PROGRESS")
    
    print(ticket)