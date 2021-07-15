# Deques são filas duplamente terminadas
import collections
import string


def main():

    # TODO: Inicialize um deque com letras minúsculas
    letrinhas = collections.deque(string.ascii_lowercase)
    # TODO: Deques suportam o método len(), mostre o tamanho da deque
    print(len(letrinhas))
    # TODO: Itere sobre a deque criada
    for letra in letrinhas:
        print(letra.upper(), end=",")
    # TODO: Manipule os itens em qualquer um dos terminais
    letrinhas.popleft()
    letrinhas.pop()
    letrinhas.append(2)
    letrinhas.appendleft(1)
    print(letrinhas)
    # TODO: Rotacione a deque
    print(letrinhas)
    letrinhas.rotate(10)
    print(letrinhas)


main()
