# Iteradores do módulo itertools
import itertools


def main():
    # Iterador cycle pode ser usado como o iter para iterar sobre uma lista
    pessoas = ["Gabriel", "Bruno", "Marvin"]
    ciclo = itertools.cycle(pessoas)
    print(next(ciclo))
    print(next(ciclo))
    print(next(ciclo))
    print(next(ciclo))
    # Usando count para criar um contador
    contador = itertools.count(100, 10)
    print(next(contador))
    print(next(contador))
    print(next(contador))
    # Usando accumulate para criar um iterador que acumula valores
    valores = [10, 20, 30, 40, 50, 40, 30]
    acumulado = itertools.accumulate(valores, max)
    print(list(acumulado))
    # Usando a função chain para conectar listas
    x = itertools.chain("ABCD", "1234")
    print(list(x))
    # Usando dropwhile e takewhile para retronar valores até uma condição
    print(list(itertools.dropwhile(condicao, valores)))
    print(list(itertools.takewhile(condicao, valores)))


def condicao(x):
    return x < 40


main()
