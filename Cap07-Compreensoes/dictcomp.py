# Usando dict comprehensions


def main():
    # Definindo uma lista de temperaturas
    ctemps = [0, 12, 34, 100]
    # Usando compreensão para construir um dicionário
    dicio_temp = {t: (t * 9/5) + 32 for t in ctemps if t < 100}
    print(dicio_temp)
    print(dicio_temp[12])


main()
