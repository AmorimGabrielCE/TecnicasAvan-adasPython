# Usando set comprehensions


def main():
    ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

    ftemp_lista = [(t * 9 / 5) + 32 for t in ctemps]
    ftemp_set = {(t * 9 / 5) + 32 for t in ctemps}
    print(ftemp_lista)
    print(ftemp_set)

    frase = "Oi eu sou o Goku"
    letras = {l.upper() for l in frase if not l.isspace()}
    print(letras)


main()
