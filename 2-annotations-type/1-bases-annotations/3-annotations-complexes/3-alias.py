from typing import TypeAlias


Couleur : TypeAlias = tuple[int, int, int]

Primitive : TypeAlias = int | str | float | bool


def ajouter(a : Primitive, b : Primitive) -> Primitive:
    return a + b #type: ignore


def creer_couleur(r : int, g : int, b : int) -> Couleur:
    return (r, g, b)