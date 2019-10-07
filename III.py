import hashlib
import random
import string

# Abre o arquivo de texto em modo append e leiturada
banco_de_dados = open("banco_de_dados.txt", "a+")

# Strings de validação
alfabeto = "abcdefghijklmnopqrsuvwxyz"
caracteres_especiais = "!@#$%¨&*()_+"
alfabeto_maiusculo = alfabeto.upper()
alfabeto_minusculo = alfabeto.lower()

# Gerador de strings aleatoria
def string_aleatoria_base16(tamanho):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(tamanho))

# Cadastra o usuário
def cadastrar_usuario(nome, senha):
    # Minuscula, maiuscula, numeral e caracteres especial são falsos por padrão
    minuscula = False 
    maiuscula = False
    numeral = False
    caracter_especial = False
    
    # Valida se o tamanho do usuário e senha é igual a 4
    if len(nome) == 4 and len(senha) == 4:

        # Percorre os caracteres de senha
        for i in range(0,len(senha)):

            # Verifica se contem uma letra minuscula
            if senha[i] in alfabeto_minusculo:
                minuscula = True 
            
            # Verifica se contem uma letra maiuscula
            elif senha[i] in alfabeto_maiusculo:
                maiuscula = True
            
            # Verifica se tem caracteres especiais
            elif senha[i] in caracteres_especiais:
                caracter_especial = True

            # Verifica se contem numerais
            try:
                numero = int(senha[i]) + 1
                numeral = True
            except:
                None

        # Caso TODAS as outras validações sejam verdadeiras, entra no if 
        if minuscula and maiuscula and numeral and caracter_especial is True:

            # Converte as entradas em string
            nome = str(nome)
            senha = str(senha)

            # Gera a salt em base hexadecimal de tamanho 16
            salt = string_aleatoria_base16(16)

            # Codifica a senha em binário
            hash_senha = hashlib.md5(senha.encode())

            # Registra os dados no arquivo de texto
            banco_de_dados.write("I I I - Método melhorado:   ")
            banco_de_dados.write("{} : {} : {}".format(nome,hash_senha.hexdigest() + salt, salt) + "\n")

        else:
            print("usuário ou senha não atendem os critérios de segurança")
    else:
        print("usuário ou senha não atendem os critérios de segurança")


# Cadastro de usuários
cadastrar_usuario("aapt", "e3A!")
cadastrar_usuario("imwl", "Aca$")
cadastrar_usuario("imtl", "@q2L")
cadastrar_usuario("aapt", "A3(a")
cadastrar_usuario("tttt", "B&34")