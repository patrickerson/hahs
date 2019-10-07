import hashlib
import random
import string


def cadastrar_usuario(nome, senha):
    # Valida o tamanho da senha e do usuário é igual a quatro
    if len(nome) == len(senha) == 4:

        # Abre p arquivo em modo append
        banco_de_dados = open("banco_de_dados.txt", "a")

        # Converte as entradas em string
        nome = str(nome)
        senha = str(senha)

        # Codifica a senha em binário
        hash_senha = hashlib.md5(senha.encode())

        # Registra os dadados
        banco_de_dados.write("I - Método sem melhorias:   ")
        banco_de_dados.write("{} : {}".format(nome,hash_senha.hexdigest()) + "\n")

    else:
        print("usuário ou senha não atendem os critérios de segurança")


cadastrar_usuario("usr1", "bola")
cadastrar_usuario("usr2", "mtbo")
cadastrar_usuario("usr3", "AqweqwD")
cadastrar_usuario("usr4", "test")
cadastrar_usuario("usr5", "aaaa")