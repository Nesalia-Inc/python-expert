

class Personne:
    def __init__(self, prenom : str, nom : str, age : int) -> None:
        self.prenom = prenom 
        self.nom = nom 
        self.age = age 
        
        
    
    def __str__(self) -> str:
        return f"Je m'appelle {self.prenom} {self.nom} et j'ai {self.age} ans."
        
    @staticmethod
    def check_noms(prenom : str, nom : str) -> bool:
        return len(prenom) < 2 or len(nom) < 2
    
    @staticmethod
    def check_age(age : int) -> bool:
        return (0 < age <= 150)
        
    @classmethod
    def create(cls, prenom : str, nom : str, age : int) -> "Personne":
        if not cls.check_noms(prenom, nom):
            raise ValueError("Le nom ou prénom contient moins de deux caractères") 
        
        if not cls.check_age(age):
            raise ValueError("L'âge n'est pas compris entre 0 et 150")
        
        return cls(prenom, nom, age)
    
    
if __name__ == '__main__':
    personne = Personne.create("Jean", "Doe", 45)
    
    print(personne)