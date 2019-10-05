import hashlib
import random
import string

alfabeto = "abcdefghijklmnopqrsuvwxyz"
caracteres_especiais = "!@#$%¨&*()_+"
alfabeto_maiusculo = alfabeto.upper()
alfabeto_minusculo = alfabeto.lower()


def cadastrar_usuario(nome, senha):
    minuscula = False 
    maiuscula = False
    numeral = False
    caracter_especial = False
    if len(nome) == 4 and len(senha) == 4:
        for i in range(0,len(senha)):
            
            if senha[i] in alfabeto_minusculo:
                minuscula = True 
            elif senha[i] in alfabeto_maiusculo:
                maiuscula = True
            elif senha[i] in caracteres_especiais:
                caracter_especial = True
            try:
                print(senha[i])
                numero = int(senha[i]) + 1
                numeral = True
            except:
                None

        if minuscula and maiuscula and numeral and caracter_especial is True:
            banco_de_dados = open("banco_de_dados.txt", "a")
            nome = str(nome)
            senha = str(senha)
            hash_senha = hashlib.md5(senha.encode())
            banco_de_dados.write("I I I - Método melhorado:   ")
            banco_de_dados.write("{} : {}".format(nome,hash_senha.hexdigest()) + "\n")

        else:
            print("usuário ou senha não atendem os critérios de segurança")
    else:
        print("usuário ou senha não atendem os critérios de segurança")

cadastrar_usuario("aapt", "e3A!")
cadastrar_usuario("imwl", "Aca$")
cadastrar_usuario("imtl", "@q2L")
cadastrar_usuario("aapt", "A3(a")
cadastrar_usuario("tttt", "B&34")