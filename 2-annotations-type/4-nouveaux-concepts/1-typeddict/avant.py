


if __name__ == '__main__':
    personne : dict[str, str | int | float] = {
        "nom" : "Jean",
        "age" : 45,
        "taille" : 1.78
    }

    personne["moteur"] = "Diesel" # Wow 
    personne["age"] = 1.25

    print(personne)