import hashlib
import random
import string


def cadastrar_usuario(nome, senha):
    if len(nome) == len(senha) == 4:
        banco_de_dados = open("banco_de_dados.txt", "a")
        nome = str(nome)
        senha = str(senha)
        hash_senha = hashlib.md5(senha.encode())
        banco_de_dados.write("I - Método sem melhorias:   ")
        banco_de_dados.write("{} : {}".format(nome,hash_senha.hexdigest()) + "\n")

    else:
        print("usuário ou senha não atendem os critérios de segurança")

cadastrar_usuario("usr1", "bola")
cadastrar_usuario("usr2", "mtbo")
cadastrar_usuario("usr3", "AqweqwD")
cadastrar_usuario("usr4", "test")
cadastrar_usuario("usr5", "aaaa")