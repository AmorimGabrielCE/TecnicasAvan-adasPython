# Uso de objetos namedtuple
import collections


def main():
    # Criando uma namedtuple para armazenar coordenadas
    coordenadas = collections.namedtuple("Coordenadas", "x y")
    p1 = coordenadas(10, 20)
    p2 = coordenadas(30, 40)

    print(p1, p2)
    print(p1.x, p2.y)
    # Usando _replace() para criar uma instância nova
    p1 = p1._replace(x=100)
    print(p1)


main()
