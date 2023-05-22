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
    if tables['cliente'].read('senha', usuario = Usuario, search_type = "usuario")[0][0] == senha:
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
    print("\n\t#####################"
            "\t### Tela de Login ###"
            "\t#####################")
          
    usuario = input("\n\tNome de usuário: ")
    if (checkUsername(usuario)):
        print("\nEsse nome de usuário ainda não possui cadastro na livraria, voltando ao menu principal...\n")
        main_menu()
        quit()

    senha = input("\tSenha: ")
    if (not checkPassword(usuario, senha)):
        print("\nA senha inserida não coincide com o usuário cadastrado, tente novamente:\n")
        main_menu()
        quit()

    loggedIn(usuario)


def Register():
    print("\n\t########################"
            "\t### Tela de Cadastro ###"
            "\t########################")
          
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
    print("Livro comprado!")
    pass


def pesquisa(p):

    search_type = {
            "T" : "titulo",
            "A" : "autor",
            "P" : "ano de publicacao"
            }[p]

    key_word = input(f"\nPor favor digite o {search_type} do livro desejado:\n-> ")
    table_livro = tables['livro']

    if p == "T":
        Titulo = key_word
        if (table_livro.read('titulo', titulo = Titulo, search_type = 'titulo')):

            print("\nLivro encontrado, deseja comprá-lo?\n")
            while True:
                encontrou = input(  
                        "* (S) Sim \n"
                        "* (N) Não \n"
                        "--> "
                        ).upper()

                if encontrou not in ["N", "S"]:
                    print("\nResposta inválida, tente novamente...")
                    continue
                else:
                    break

            if encontrou == "S":
                compra(Titulo)
            else:
                print("\nCompra cancelada")
            
        else:
            print(f"\nNenhum livro no estoque da livraria possui o título '{Titulo}'")

    elif p == "A":
        Autor = key_word
        #a ser testado
        if (ret := table_livro.read('autor', autor = Autor, search_type = 'autor')):

            print(f"\nLivros escritos por {Autor}:")
            for row in ret:
                print("  - " + row[0])
        else:
            print(f"\nNenhum livro no estoque da livraria foi escrito por '{Autor}'")
    
    else:
        anoPublicacao = key_word
        #a ser testado
        if (ret := table_livro.read('titulo', ano_publicacao = anoPublicacao, search_type = 'ano_publicacao')):
            print(f"\nLivros publicados no ano de {anoPublicacao}:")
            for row in ret:
                print("  - " + row[0])
        else:
            print(f"\nNenhum livro no estoque da livraria foi publicado no ano de {anoPublicacao}")
    
    print("\nVoltando ao menu principal...\n")
    main_menu()
    quit()


def bookSearch():
    search_c = ["T", "A", "P"]

    print("\nAqui você consegue consultar os livros contidos no estoque da nossa livraria:\n")

    while True:
        p = input(  
                "* (T) Pesquisa por título \n"
                "* (A) Pesquisa por autor \n"
                "* (P) Pesquisa por ano de publicação \n\n"
                "-> "
                )
        p = p.upper()

        if p not in search_c:
            print("\nDesculpe, tente novamente...\n")
            continue
        else:
            break

    pesquisa(p)


def quitLibrary():
    print("\n\tObrigado por visitar a livraria Tuko!\n")
    quit()


def main_menu():
    menu_c = ["L", "C", "P", "Q"]

    print("O que deseja fazer?")
    while True:
        choice = input( 
                "* (L) Realizar login \n"
                "* (C) Realizar cadastro \n"
                "* (P) Pesquisar livro sem cadastro \n"
                "* (Q) Sair do sistema \n"
                "-> "
                )

        choice = choice.upper()

        if choice not in  menu_c:
            print("\nDesculpe, tente novamente...\n")
            continue
        else:
            break

    

    if choice   == "L":
        Login()
    elif choice == "C":
        Register()
    elif choice == "P":
        bookSearch()
    elif choice == "Q":
        quitLibrary()
    else:
        print("Deu ruim")
        exit(-666)
    





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
    print("\n\t########################################################\n"
            "\t######## Olá seja bem vindo a livraria Tuko! ###########\n"
            "\t########################################################\n")
    main_menu()

if __name__ == "__main__":
    main()

