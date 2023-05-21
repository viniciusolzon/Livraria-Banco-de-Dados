# import os
# import pandas as pd
# from sqlalchemy import create_engine
from tabelas.gerador import tables

# Limpa o terminal
# def clear_terminal():
#     os.system('cls' if os.name == 'nt' else 'clear')


def checkEmail(Email):
    # checa se o email existe na tabela "cliente", se existe fala "O email inserido já possui cadastro na livraria"
    if tables['cliente'].read('email', email = Email, search_type = "email"):
        return False
    # se não, ele vai pra próxima etapa de registro
    return True


def checkUsername(Usuario):
    # checa se o nome do usuário existe na tabela "cliente", se não, para e fala: "Usuário não encontrado no registro"
    if tables['cliente'].read('usuario', usuario = Usuario, search_type = "usuario"):
        return False
    # se não, ele vai pra próxima etapa de registro
    return True


def checkPassword(Usuario, senha):
    # checa se a senha do usuário coincide com a senha registrada desse usuaŕio na tabela "cliente"
    if tables['cliente'].read('senha', usuario = Usuario, search_type = "usuario") == senha:
        return True
    # se digitada corretamente, libera o login
    return False


def loggedIn(usuario):
    print(f"\n\tBem vindo de volta {usuario}!\n")
    quit()


def registered(name, usuario, email, senha):
    tables['cliente'].insert(name, usuario, email, senha)
    print("\n\tRegistro feito com sucesso!\n")
    main_menu()
    quit()


def Login():
    print("""\n\t#####################
\t### Tela de Login ###
\t#####################""")
          
    usuario = input("\n\tNome de usuário: ")
    if(checkUsername(usuario)):
        print("\nEsse nome de usuário ainda não possui cadastro na livraria, voltando ao menu principal...\n")
        main_menu()
        quit()

    senha = input("\tSenha: ")
    if(not checkPassword(usuario, senha)):
        print("\nA senha inserida não coincide com o usuário cadastrado, tente novamente:\n")
        main_menu()
        quit()

    loggedIn(usuario)


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

    usuario = input("\tNome de usuário: ")
    if(not checkUsername(usuario)):
        print("\nEsse nome de usuário já possui cadastro na livraria, voltando ao menu principal...\n")
        main_menu()
        quit()

    senha = input("\tSenha: ")
    senha_verificacao = input("\tVerificação da senha: ")
    while senha != senha_verificacao:
        print("\n\tAs senhas digitadas não coincidem, por favor tente novamente:")
        senha = input("\tSenha: ")
        senha_verificacao = input("\tVerificação da senha: ")

    registered(name, usuario, email, senha)


def compra(titulo):
    print("Comprado")
    pass


def pesquisa(p):
    if p.upper() == "T":
        Titulo = input("\nPor favor digite o título do livro desejado:\n-> ")
        if(tables['livro'].read('titulo', titulo = Titulo, search_type = 'titulo')):
            encontrou = input("\nLivro encontrado, deseja comprá-lo?\n* Sim (s)\n* Não (n)\n")
            while(encontrou.upper() != "S" and encontrou.upper() != "N"):
                encontrou = input("\nDesculpe, tente novamente...\nLivro encontrado, deseja comprá-lo?\n* Sim (s)\n* Não (n)\n")
            if(encontrou.upper() == "S"):
                compra(Titulo)
            else:
                print("\nCompra cancelada")
            
        else:
            print(f"\nNenhum livro no estoque da livraria possui o título '{Titulo}'")

    elif p.upper() == "A":
        Autor = input("\nPor favor digite o autor do livro desejado:\n-> ")
        if(tables['livro'].read('autor', autor = Autor, search_type = 'autor')):
            print(f"\nLivros escritos por {Autor}:")
            for row in tables['livro'].read('titulo', autor = Autor, search_type = 'autor'):
                print("  - " + row[0])
        else:
            print(f"\nNenhum livro no estoque da livraria foi escrito por '{Autor}'")
    
    else:
        anoPublicacao = input("\nPor favor digite o ano de publicação do livro desejado:\n-> ")
        if(tables['livro'].read('titulo', ano_publicacao = anoPublicacao, search_type = 'ano_publicacao')):
            print(f"\nLivros publicados no ano de {anoPublicacao}:")
            for row in tables['livro'].read('titulo', ano_publicacao = anoPublicacao, search_type = 'ano_publicacao'):
                print("  - " + row[0])
        else:
            print(f"\nNenhum livro no estoque da livraria foi publicado no ano de {anoPublicacao}")
    
    print("\nVoltando ao menu principal...\n")
    main_menu()
    quit()


def bookSearch():
    p = input("\nAqui você consegue consultar os livros contidos no estoque da nossa livraria:\n* Pesquisa por título (T)\n* Pesquisa por autor (A)\n* Pesquisa por ano de publicação (P)\n\n-> ")
    while(p.upper() != "T" and p.upper() != "A" and p.upper() != "P"):
        p = input("\nDesculpe, tente novamente...\nPesquisa por título (T)\n* Pesquisa por autor (A)\n* Pesquisa por ano de publicação (P)\n\n-> ")
    pesquisa(p)


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
    else:
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

# def main():
#     # Create an engine instance
#     alchemyEngine   = create_engine('postgresql+psycopg2://postgres:1234@localhost:5432')
#     # Connect to PostgreSQL server
#     dbConnection    = alchemyEngine.connect()
#     # Create a dataframe
#     clienteDF = pd.read_sql_query("SELECT * FROM cliente;", dbConnection)
#     livroDF = pd.read_sql_query("SELECT * FROM livro;", dbConnection)

#     print(clienteDF.head())
#     print(livroDF.head())
    
#     get_books()
#     get_users()
# Testando o uso de dataFrames^^^^^^^^^^^^^

def main():
    print("""\n\t########################################################
\t######## Olá seja bem vindo a livraria Tuko! ###########
\t########################################################\n""")
    main_menu()

if __name__ == "__main__":
    main()

