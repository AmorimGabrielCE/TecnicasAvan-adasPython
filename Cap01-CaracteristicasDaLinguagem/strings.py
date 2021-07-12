#Strings e bytes não são diretamente intercambiáveis
#Strings contém unicode, bytes são valores de 8 bits


def main():
    #Definindo valores iniciais
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s = "Isso é uma string"
    print(s)

    #Tentando juntar os dois.
    #print(s + b)

    #Bytes e strings precisam ser encoded e decoded
    print(s + b.decode(('utf-8')))

    #Fazendo encode da string como UTF-32
    print(s.encode('utf-32') + b)



if __name__ == "__main__":
    main()


