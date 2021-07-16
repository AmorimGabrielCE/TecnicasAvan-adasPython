# Uso do módulo logging

import logging


def main():
    # Usando basicConfig para confgurar o logging
    logging.basicConfig(level=logging.DEBUG,
                        filename='output.log')

    # Testando os níveis de log
    logging.debug("Esta é uma mensagem de debug")
    logging.info("Esta é uma mensagem de informação")
    logging.warning("Esta é uma mensagem de aviso")
    logging.error("Esta é uma mensagem de erro")
    logging.critical("Esta é uma mensagem crítica")


main()
