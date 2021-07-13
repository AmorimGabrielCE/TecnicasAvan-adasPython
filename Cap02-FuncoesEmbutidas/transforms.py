# Usando funções transformadoras: sorted, filter, map
numeros = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
letras = "abcDeFGHiJklmnoP"


def transformadoras():
    notas = (81, 89, 94, 78, 61, 66, 99, 74)
    # Usando filter para remover itens de uma lista
    impares = list(filter(primeiro_filtro, numeros))
    print(impares)
    # Usando filter numa sequência de caracteres
    minusculas = list(filter(segundo_filtro, letras))
    print(minusculas)
    # Usando map para criar uma nova sequência de valores
    quadrados = list(map(quadrado, numeros))
    print(quadrados)
    # Usando sorte e map para mudar as notas para conceito
    notas = sorted(notas)
    conceito = list(map(notas_para_conceito, notas))
    print(conceito)


def primeiro_filtro(x):
    if x % 2 == 0:
        return False
    return True


def segundo_filtro(x):
    if x.isupper():
        return False
    return True


def quadrado(x):
    return x**2


def notas_para_conceito(x):
    if x >= 90:
        return "A"
    elif x >= 90:
        return "A"
    elif 90 > x >= 80:
        return "B"
    elif 80 > x >= 70:
        return "C"
    elif 70 > x >= 65:
        return "D"
    elif x < 65:
        return "F"


transformadoras()
