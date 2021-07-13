#Demonstração de algumas funções built-in úteis.

def main():
    # Usando any() e all() para testar valores boleanos
    lista = [1, 2, 3, 4, 5, 6]
    # Retorna true caso qualquer valor da lista seja verdade
    print(any(lista))
    # Retorna True se todos os valores da lista forem verdade
    print(all(lista))
    # Usando as funções min e max para retornar os valores mínimo e máximo
    print(min(lista))
    print(max(lista))
    # Usando sum() para somar os valores da lista
    print(sum(lista))



if __name__ == "__main__":
    main()