


class SoftwareVersion:
    def __init__(self, majeure: int, mineure: int, patch: int) -> None:
        self.majeure = majeure
        self.mineure = mineure
        self.patch = patch

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SoftwareVersion):
            return NotImplemented
        return (self.majeure, self.mineure, self.patch) == (other.majeure, other.mineure, other.patch)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, SoftwareVersion):
            return NotImplemented
        return (self.majeure, self.mineure, self.patch) < (other.majeure, other.mineure, other.patch)

    def __le__(self, other: object) -> bool:
        return self == other or self < other

    def __gt__(self, other: object) -> bool:
        return not self <= other

    def __ge__(self, other: object) -> bool:
        return not self < other

    def __ne__(self, other: object) -> bool:
        return not self == other

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
