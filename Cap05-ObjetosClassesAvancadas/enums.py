# Define enumerations usando the Enum base class
from enum import Enum, auto


# Definindo uma classe Fruta que herda de Enum
class Fruta(Enum):
    UVA = 1
    BANANA = 2
    LARANJA = 3
    TOMATE = 4
    PERA = auto()


def main():
    # Objetos enum possuem valores e tipos de fácil leitura
    print(Fruta.UVA)
    print(type(Fruta.UVA))
    print(repr(Fruta.UVA))
    # Objetos enum possuem prorpriedades "name" e "value"
    print(Fruta.UVA.name, Fruta.UVA.value)
    # Mostrando o valor gerado automaticamente para PERA
    print(Fruta.PERA.value)
    # É possivel usar objetos enum como chaves
    frutas = dict()
    frutas[Fruta.BANANA] = "Casca amarela"
    print(frutas[Fruta.BANANA])


main()
