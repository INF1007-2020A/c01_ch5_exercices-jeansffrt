#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

from typing import List


def convert_to_absolute() -> float:
    value = float(input("number : "))
    return abs(value)


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOP', 'ack'
    names  = []
    for prefixe in prefixes:
        names.append(prefixe + suffixes)
    return names


def prime_integer_summation() -> int:
    nombre_de_nombres_premiers = 0
    somme = 0
    nombre = 1
    while nombre_de_nombres_premiers < 100:
        premier = True
        if nombre > 1:
            for diviseur in range(2, nombre):
                if nombre % diviseur == 0:
                    premier = False
                    break
        if premier:
            somme += nombre
            nombre_de_nombres_premiers += 1
        nombre += 1
    return somme


def factorial(number: int) -> int:
    return math.factorial(number)


def use_continue() -> None:
    for i in range(11):
        if i == 5: continue
        else: print(i)


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
