


class SoftwareVersion:
    def __init__(self, majeure: int, mineure: int, patch: int) -> None:
        self.majeure = majeure
        self.mineure = mineure
        self.patch = patch


    # La dunder method `__eq__` est appelée lorsqu'on utilises l'opérateur `==`
    # entre deux objets de la classe. Théoriquement, il doit renvoyer si oui ou non
    # ces deux objets sont égaux. Techniquement, tu retournes la valeur booléenne que tu veux,
    # rien ne t'es forcé sur le calcul à faire pour avoir le résultat. 
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, SoftwareVersion):
            return NotImplemented
        return (self.majeure, self.mineure, self.patch) == (value.majeure, value.mineure, value.patch)

    # La dunder method `__lt__` est appelée lorsqu'on utilises l'opérateur `<`. 
    # Son fonctionnement est exactement le même que `__eq__`. 
    def __lt__(self, value: object) -> bool:
        if not isinstance(value, SoftwareVersion):
            return NotImplemented
        return (self.majeure, self.mineure, self.patch) < (value.majeure, value.mineure, value.patch)

    # Une fois que les opérations `==` et `<` ont été définies, 
    # il est possible de définir toutes les autres opérations avec elles. 
    
    def __le__(self, value: object) -> bool: # Appelée avec l'opérateur <=
        return self == value or self < value

    def __gt__(self, value: object) -> bool: # Appelée avec l'opérateur >
        return not self <= value

    def __ge__(self, value: object) -> bool: # Appelée avec l'opérateur >=
        return not self < value

    def __ne__(self, value: object) -> bool: # Appelée avec l'opérateur !=
        return not self == value

    def __str__(self) -> str:
        return f"{self.majeure}.{self.mineure}.{self.patch}"











version1 = SoftwareVersion(1, 2, 3)
version2 = SoftwareVersion(1, 2, 4)
version3 = SoftwareVersion(1, 2, 3)

print(version1 == version2)
print(version1 < version2) 
print(version1 <= version2)
print(version1 > version2) 
print(version1 >= version2)
print(version1 != version2)
print(version1 == version3)

print(version1)
print(version2)
print(version3)
