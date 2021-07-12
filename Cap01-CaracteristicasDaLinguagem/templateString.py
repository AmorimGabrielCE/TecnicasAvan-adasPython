from string import Template


def main():
    #Fomatação tradicional usando o format()
    frase = "Você está assistindo {0} com {1}".format("Python Avançado",
        "Jessica Temporal")
    print(frase)

    #Criando template com placeholders
    templ = Template("Você está assistindo ${curso} com ${instrutora}")

    #Usando o sunstitute com argumentos nomeados
    frase2 = templ.substitute(
        curso="Python Avançado",
        instrutora="Jessica Temporal"
    )
    print(frase2)

    #Usando o método subtitute com um dicionário
    dados = {
        "curso": "Python Avançado",
        "instrutora": "Jessica Temporal"
    }
    frase3 = templ.substitute(dados)
    print(frase3)


if __name__ == "__main__":
    main()