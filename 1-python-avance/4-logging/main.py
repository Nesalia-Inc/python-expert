import logging

logger = logging.getLogger(__name__)

logging.basicConfig(
    filename="log.log",
    level=logging.DEBUG,
    encoding="utf-8",
    format='%(levelname)s:%(asctime)s:%(message)s',
    datefmt='%d/%m/%Y-%I:%M:%S',
    filemode="w"
)



class Animal:
    def __init__(self, nom : str, age : int) -> None:
        self.nom = nom
        self.age = age


    def __str__(self) -> str:
        logging.info("Affichage des informations d'un animal")
        return f"{self.nom}, Age: {self.age} ans"


class Chien(Animal):
    pass 

class Chat(Animal):
    pass 



class Animalerie:
    def __init__(self) -> None:
        self.animaux : list[Animal] = []


    def ajouter_animal(self, animal : Animal) -> None:
        self.animaux.append(animal)
        logging.info("Ajout d'un animal dans l'animalerie")
        print(f"{animal} a été ajouté à l'animalerie.")

    def afficher_animaux(self) -> None:
        if not self.animaux:
            logging.error("Aucun animal dans l'animalerie")
            print("Aucun animal dans l'animalerie.")
        else:
            for animal in self.animaux:
                print(animal)

    def supprimer_animal(self, nom : str) -> None:
        for animal in self.animaux:
            if animal.nom == nom:
                self.animaux.remove(animal)
                
                logging.info("Animal supprimé de l'animalerie")
                print(f"{animal} a été supprimé de l'animalerie.")
                return
            
        logging.error("Animal non trouvé")
        print(f"Aucun animal nommé {nom} n'a été trouvé dans l'animalerie.")





def afficher_menu():
    print("\n--- Menu de l'Animalerie ---")
    print("1. Ajouter un animal")
    print("2. Afficher les animaux")
    print("3. Supprimer un animal")
    print("4. Quitter")

def main():
    animalerie = Animalerie()
    
    while True:
        afficher_menu()
        choix = input("Choisissez une option: ")
        
        if choix == '1':
            type_animal = input("Quel type d'animal voulez-vous ajouter (chien/chat) ? ")
            nom = input("Nom de l'animal: ")
            age = int(input("Âge de l'animal: "))
            
            if type_animal.lower() == "chien":
                animal = Chien(nom, age)
            elif type_animal.lower() == "chat":
                animal = Chat(nom, age)
            else:
                print("Type d'animal non reconnu.")
                continue
            
            animalerie.ajouter_animal(animal)
        
        elif choix == '2':
            animalerie.afficher_animaux()
        
        elif choix == '3':
            nom = input("Nom de l'animal à supprimer: ")
            animalerie.supprimer_animal(nom)
        
        elif choix == '4':
            print("Au revoir!")
            break
        
        else:
            print("Choix non valide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
