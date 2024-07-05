from enum import Enum, auto 


# On défini une nouvelle énumération en faisant
# hériter une classe de `Enum`. 
class Status(Enum):
    
    # On défini les éléments d'une énumération comme des variables d'instances. 
    # Par convention, on doit leur mettre la syntaxe d'une constante. Lorsque 
    # la valeur d'une énumération n'est pas importante, on utilises la 
    # fonction `auto` qui a comme rôle de donner la valeur `1` au premier 
    # élément, `2` au second, etc.
    OPEN = auto()
    IN_PROGRESS = auto()
    CLOSED = auto()
    
    
    # Il est possible de rajouter des méthodes dans une énumération. 
    # Généralement, je les utilises comme méthodes utilitaires comme ici. 
    # Le but de cette méthode est simplement de passer au status suivant 
    # d'un status donné tout en veillant à bien revenir au début si nécessaire
    def next(self) -> "Status":
        all_status = list(Status)
        index = all_status.index(self)
        
        return all_status[(index + 1) % len(all_status)]
    
    
class Priority(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()

    # Il est possible de définir des alias aux valeurs de nos énumérations
    # Ca veut donc dire que `Priority.NORMAL == Priority.LOW` renvoie `True`. 
    # C'est très pratique dans certains cas mais peut créer une confusion 
    # pour l'utilisateur de l'énumération.
    NORMAL = LOW    
    IMPORTANT = MEDIUM
    URGENT = HIGH
    
    
    
class Ticket:
    def __init__(self, title : str, description : str, priority : Priority):
        self.title = title
        self.description = description
        self.priority = priority
        
        # On peut récupérer les éléments d'une énumération comme des variables
        # d'instance classique c'est-à-dire `Classe.variable`. On peut techniquement 
        # `self.status.value` pour récupérer sa valeur (`1`) et `self.status.name` 
        # pour récupérer le nom de cet élément dans l'énumération càd `OPEN` 
        self.status = Status.OPEN
    
    def __str__(self) -> str:
        return f"Ticket(title={self.title}, description={self.description}, priority={self.priority.name}, status={self.status.name})"
    
    # Les deux méthodes d'update ne sont plus nécessaires puisqu'elles étaient 
    # uniquement présentes pour vérifier que la nouvelle valeur du status/priorité
    # étaient bien correctes. Ici, aucune erreur n'est possible puisque les valeurs
    # sont limités par celles qui se trouvent dans l'énumération. Le code est donc 
    # plus clair mais aussi plus simple !
    



if __name__ == "__main__":
    ticket = Ticket(
        "Bug dans le système de connection",
        "Le client ne peut pas se connecter",
        Priority.HIGH
        ) 
    
    ticket.status = ticket.status.next()
    
    print(ticket)
    