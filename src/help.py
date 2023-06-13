from tabelas.gerador import tables
import os

# Limpa o terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fecha o sistema
def quitLibrary():
    print("\n\tFechando o sistema...")
    print("\n\tObrigado por visitar a livraria Tuko!\n")
    quit()

# Usuario escolhe sim ou não
def SimNao():
    while True:
        escolha = input(  
                "* (S) Sim \n"
                "* (N) Não \n"
                "-> "
                ).upper()

        if escolha not in ["N", "S", "SIM", "NAO", "NÃO"]:
            print("\nResposta inválida, tente novamente...")
            continue
        else:
            return escolha

# Usuario escolhe voltar
def Voltar():
    opcoes = ["V", "VOLTAR"]

    while True:
        voltar = input(
                "\n* (V) Voltar\n"
                "-> "
                )

        voltar = voltar.upper()

        if voltar not in opcoes:
            print("\nDesculpe, tente novamente...\n")
            continue
        else:
            clear_terminal()
            break

# checa se o email existe na tabela "cliente", se existe fala "O email inserido já possui cadastro na livraria"
def checkEmail(Email):
    cliente_cadastrado = tables['cliente'].read('email', email = Email, search_type = "email")
    funcionario_cadastrado = tables['vendedor'].read('email', email = Email, search_type = "email")

    if cliente_cadastrado or funcionario_cadastrado:
        return False
    # se não, ele vai pra próxima etapa de registro
    return True

# checa se o nome do usuário existe na tabela "cliente", se não, para e fala: "Usuário não encontrado no registro"
def checkUsername(Usuario):
    cliente_cadastrado = tables['cliente'].read('usuario', usuario = Usuario, search_type = "usuario")
    funcionario_cadastrado = tables['vendedor'].read('usuario', usuario = Usuario, search_type = "usuario")
    
    if cliente_cadastrado or funcionario_cadastrado:
        return False
    # se não, ele vai pra próxima etapa de registro
    return True

# checa se a senha do usuário coincide com a senha registrada desse usuaŕio na tabela "cliente"
def checkPassword(Usuario, senha):
    cliente = tables['cliente'].read('*', usuario = Usuario, search_type = "usuario")
    funcionario = tables['vendedor'].read('*', usuario = Usuario, search_type = "usuario")

    if funcionario:
        senha_funcionario = tables['vendedor'].read('senha', usuario = Usuario, search_type = "usuario")[0][0]
        if senha_funcionario == senha:
            return True
        else:
            return False
            
    elif cliente:
        senha_cliente = tables['cliente'].read('senha', usuario = Usuario, search_type = "usuario")[0][0]
        if senha_cliente == senha:
            return True
        else:
            return False
