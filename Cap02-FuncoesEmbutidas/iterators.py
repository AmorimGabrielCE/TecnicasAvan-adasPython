# Usando funções iteradoras como enumerate, zip, iter, next

def iteradoras():
    dias = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sab"]
    dias_en = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    # Usando a função iter para criar um iterador sobre uma lista
    iterador_dias = iter(dias)
    print(next(iterador_dias))
    print(next(iterador_dias))
    print(next(iterador_dias))
    # Usando iter para iterar sobre um arquivo
    """with open('Cap02-FuncoesEmbutidas\\dados.txt', 'r') as fp:
        for linha in iter(fp.readline(), ''):
            print(linha)"""
    # Usando a iteração tradicional
    for numero in range(len(dias)):
        print(numero, dias[numero])
    # Usando enumerate para reduzir o código e ter um contador
    for i, dia in enumerate(dias):
        print(i, dia)
    # Usando zip para juntar listas
    for d in zip(dias, dias_en):
        print(d)
    # Combinando zip e enumerate para formatar o resultado
    for i, d in enumerate(zip(dias, dias_en)):
        print(i, d[0], "=", d[1], "em Inglês")


iteradoras()
