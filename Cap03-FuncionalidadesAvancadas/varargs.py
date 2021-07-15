def adicao(*args):
    return sum(args)


def main():
    # Passando argumentos para o método
    print(adicao(5, 10, 30))
    print(adicao(5, 5, 5))
    # Passando uma lista para o método
    valores = (5, 10, 15, 20)
    print(adicao(*valores))

main()