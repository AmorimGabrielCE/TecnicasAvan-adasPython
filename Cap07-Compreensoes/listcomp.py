# Usando list comprehensions


def main():
    # Definindo duas lista de números pares e ímpares
    pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # Usando map() e list() para calcular números ao quadrado
    pares_quadrado = list(map(lambda n: n**2, pares))
    print(pares_quadrado)

    # Criando uma lista nova a partir de uma preexistente
    pares_quadrado2 = [n**2 for n in pares]
    print(pares_quadrado2)

    # Usando o predicado para limitar os itens
    impares_quadrado = [n ** 2 for n in impares if 7 < n < 15]
    print(impares_quadrado)


main()
