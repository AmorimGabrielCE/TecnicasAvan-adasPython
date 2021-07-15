# Usando objetos defaultdict
import collections


def main():
    # Definindo uma lista para contar
    frutas = ['maçã', 'pêra', 'laranja', 'banana', 'maçã', 'uva', 'banana',
              'banana']

    # Usando um dicionário default para contar cada elemento
    contador_frutas = collections.defaultdict(int)

    # Contando os elementos da lista
    for fruta in frutas:
        contador_frutas[fruta] += 1

    # Imprimindo o resultado
    for (c, v) in contador_frutas.items():
        print(c + ": " + str(v))


main()
