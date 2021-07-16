# Personalizando o retorno do loggin
import logging

dados = {"pessoa": "jess"}


# Criando outra função para rodar o log
def outra_funcao():
    logging.info("Esta é uma mensagem de informação", extra=dados)


def main():
    # TODO: Defina o nível de log para debug e um arquivo para salvar
    # o retorno. Use também uma formatação personalizada
    formato = "%(asctime)s: %(levelname)s: %(funcName)s: Pessoa: %(pessoa)s"
    logging.basicConfig(level=logging.DEBUG,
                        filename='CustomOutput.log',
                        format=formato)

    logging.info("Esta é uma mensagem de informação", extra=dados)
    logging.warning("Esta é uma mensagem de aviso", extra=dados)


main()
outra_funcao()
