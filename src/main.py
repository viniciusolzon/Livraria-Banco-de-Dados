from initializer import tables
from sqlalchemy import create_engine
import pandas as pd
import os

# Limpa o terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def checkEmail(email):
    # checa se o email existe na tabela "cliente", se existe fala "O email inserido já possui cadastro na livraria"
    if tables['cliente'].read(email, search_type = "email"):
        return False
    # se não, ele vai pra próxima etapa de registro
    return True


def checkUsername(username):
    # checa se o nome do usuário existe na tabela "cliente", se não, para e fala: "Usuário não encontrado no registro"
    if tables['cliente'].read(username, search_type = "username"):
        return False
    # se não, ele vai pra próxima etapa de registro
    return True

def checkPassword(username, pswd):
    # checa se a senha do usuário coincide com a senha registrada desse usuaŕio na tabela "cliente"
    if tables['cliente'].read(username, search_type = "password")[0][0] == pswd:
        return True
    # se digitada corretamente, libera o login
    return False

def loggedIn(username):
    print(f"\n\tBem vindo de volta {username}!\n")

def registered(name, username, email, password):
    tables['cliente'].insert(name, username, password, email)
    print("\n\tRegistro feito com sucesso!\n")

def Login():
    print("""\n\t#####################
\t### Tela de Login ###
\t#####################""")
          
    username = input("\n\tNome de usuário: ")
    if(checkUsername(username)):
        print("\nUsuário ainda não possui cadastro na livraria, voltando ao menu principal...\n")
        main_menu()
        quit()
        
    pswd = input("\tSenha: ")
    if(not checkPassword(username, pswd)):
        print("\nA senha inserida não coincide com o usuário cadastrado, tente novamente:\n")
        main_menu()
        quit()

    loggedIn(username)

def Register():
    print("""\n\t########################
\t### Tela de Cadastro ###
\t########################""")
          
    name = input("\n\tNome completo: ")
    # aqui não precisa de verificação nenhuma pq podem existir vários usuários com o mesmo nome

    email = input("\tEmail: ")
    if(not checkEmail(email)):
        print("\nO email inserido já possui cadastro na livraria, voltando ao menu principal...\n")
        main_menu()
        quit()


    username = input("\tNome de usuário: ")
    if(not checkUsername(username)):
        print("\nEsse nome de usuário já possui cadastro na livraria, voltando ao menu principal...\n")
        main_menu()
        quit()

    pswd = input("\tSenha: ")
    pswd_verification = input("\tVerificação da senha: ")
    while pswd != pswd_verification:
        print("\n\tAs senhas digitadas não coincidem, por favor tente novamente:")
        pswd = input("\tSenha: ")
        pswd_verification = input("\tVerificação da senha: ")

    registered(name, username, email, pswd)

def bookSearch():
    pesquisa = input("\nAqui você consegue consultar os livros contidos no estoque da nossa livraria:\n* Pesquisa por título (T)\n* Pesquisa por autor (A)\n* Pesquisa por ano de publicação (P)\n* Pesquisa por gênero (G)\n\n-> ")
    while(pesquisa.upper() != "T" and pesquisa.upper() != "A" and pesquisa.upper() != "P" and pesquisa.upper() != "G"):
        pesquisa = input("\nDesculpe, tente novamente...\nPesquisa por título (T)\n* Pesquisa por autor (A)\n* Pesquisa por ano de publicação (P)\n* Pesquisa por gênero (G)\n\n-> ")

def quitLibrary():
    print("\n\tObrigado por visitar a livraria Tuko!\n")
    quit()

def main_menu():
    choice = input("O que deseja fazer?\n* Realizar login (L)\n* Realizar cadastro (C)\n* Pesquisar livro sem cadastro (P)\n* Sair do sistema (Q)\n-> ")
    while(choice.upper() != "L" and choice.upper() != "C" and choice.upper() != "P" and choice.upper() != "Q"):
        choice = input("\nDesculpe, tente novamente...\n* Realizar login (L)\n* Realizar cadastro (C)\n* Pesquisar livro sem cadastro (P)\n\n-> ")
    if choice.upper() == "L":
        Login()
    elif choice.upper() == "C":
        Register()
    elif choice.upper() == "P":
        bookSearch()
    elif choice.upper() == "Q":
        quitLibrary()
    




# Testando o uso de dataFrames^^^^^^^^^^^^^
def get_books():
    for row in tables['livro'].read_all():
        print(row)
    print()

def get_users():
    for row in tables['cliente'].read_all():
        print(row)
    print()

def main():
    # Create an engine instance
    alchemyEngine   = create_engine('postgresql+psycopg2://postgres:1234@localhost:5432')
    # Connect to PostgreSQL server
    dbConnection    = alchemyEngine.connect()
    # Create a dataframe
    clienteDF = pd.read_sql_query("SELECT * FROM cliente;", dbConnection)
    livroDF = pd.read_sql_query("SELECT * FROM livro;", dbConnection)

    print(clienteDF.head())
    print(livroDF.head())
    
    # get_books()
    # get_users()
# Testando o uso de dataFrames^^^^^^^^^^^^^



if __name__ == "__main__":
    # main()
    print("""\n\t########################################################
\t######## Olá seja bem vindo a livraria Tuko! ###########
\t########################################################\n""")
    main_menu()
