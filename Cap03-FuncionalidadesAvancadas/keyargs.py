# Uso de argumentos nomeados

def minha_funcao(arg1, arg2, *, suprimir_exceptions=False):
    print(arg1, arg2, suprimir_exceptions)


def main():
    # Tentando fazer a chamada da função sem o nome do argumento
    # minha_funcao(1, 2, True)
    # Maneira correta
    minha_funcao(1, 2, suprimir_exceptions=True)


main()
