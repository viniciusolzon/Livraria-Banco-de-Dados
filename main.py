# import os
# import pandas as pd
# from sqlalchemy import create_engine
from tabelas.gerador import tables

# Limpa o terminal
# def clear_terminal():
#     os.system('cls' if os.name == 'nt' else 'clear')

loggedIn = False

def SimNao():
    while True:
        escolha = input(  
                "* (S) Sim \n"
                "* (N) Não \n"
                "-> "
                ).upper()

        if escolha not in ["N", "S"]:
            print("\nResposta inválida, tente novamente...")
            continue
        else:
            return escolha

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
        # print("\n\tEsse nome de usuário ainda não possui cadastro na livraria, voltando ao menu principal...\n")
        print("\n\tEsse nome de usuário ainda não possui cadastro na livraria, deseja fazer o cadastro?\n")
        deseja = SimNao()

        if deseja == "S":
            Register()
        else:
            print("\nVoltando ao menu principal...\n")
            main_menu()
            quit()

    senha = input("\tSenha: ")
    if (not checkPassword(usuario, senha)):
        print("\n\tA senha inserida não coincide com o usuário cadastrado, tente novamente:\n")
        senha = input("\tSenha: ")
        if (not checkPassword(usuario, senha)):
            print("\n\tA senha inserida não coincide com o usuário cadastrado, voltando ao menu principal...\n")
            main_menu()
            quit()

    loggedIn = True
    menuloggedIn(loggedIn)
    quit()


def Register():
    print("\n\t######################"
            "  ### Tela de Cadastro ###  "
            "######################")
          
    name = input("\n\tNome completo: ")
    # aqui não precisa de verificação nenhuma pq podem existir vários usuários com o mesmo nome

    email = input("\tEmail: ")
    if(not checkEmail(email)):
        print("\n\tO email inserido já possui cadastro na livraria, voltando ao menu principal...\n")
        main_menu()
        quit()

    usuario = input("\tNome de usuário: ")
    if(not checkUsername(usuario)):
        print("\n\tEsse nome de usuário já possui cadastro na livraria, voltando ao menu principal...\n")
        main_menu()
        quit()

    senha = input("\tSenha: ")
    senha_verificacao = input("\tVerificação da senha: ")
    
    if senha != senha_verificacao:
        print("\n\tAs senhas digitadas não coincidem, por favor tente novamente:")
        senha = input("\tSenha: ")
        senha_verificacao = input("\tVerificação da senha: ")
        
    if senha != senha_verificacao:
        print("\n\tAs senhas digitadas não coincidem, voltando ao menu principal...\n")
        main_menu()
        quit()

    registered(name, usuario, email, senha)


def compra():
    print("Livro comprado!")
    pass


def pesquisa(p, loggedIn):

    search_type = {
            "T" : "titulo",
            "A" : "autor",
            "P" : "ano de publicacao"
            }[p]

    key_word = input(f"\nPor favor informe o {search_type} do livro desejado:\n-> ")
    table_livro = tables['livro']

    if p == "T":
        Titulo = key_word
        if (table_livro.read('titulo', titulo = Titulo, search_type = 'titulo')):

            if loggedIn:
                print("\nLivro encontrado, deseja comprá-lo?\n")
                comprar = SimNao()
                if comprar == "S":
                    compra()
                else:
                    print("\nCompra cancelada")
                    print("\nVoltando ao menu da sua conta...\n")
                    menuloggedIn(loggedIn)
            else:
                print("\nLivro encontrado, deseja fazer login para comprá-lo?\n")
                deseja = SimNao()
                if deseja == "S":
                    Login()
                else:
                    print("\nVoltando ao menu principal...\n")
                    main_menu()
                    


        else:
            print(f"\nNenhum livro no estoque da livraria possui o título '{Titulo}'")
            if loggedIn:
                print("\nVoltando ao menu da sua conta...\n")
                menuloggedIn(loggedIn)
            else:
                print("\nVoltando ao menu principal...\n")
                main_menu()

    elif p == "A":
        Autor = key_word
        if (ret := table_livro.read('titulo', autor = Autor, search_type = 'autor')):

            print(f"\nLivros escritos por {Autor}:")
            i = 0
            for row in ret:
                i +=1
                print(f" {i} - {row[0]}")

            if loggedIn:
                print("\nDeseja comprar algum livro destacado acima?\n")
                comprar = SimNao()
                if comprar == "S":
                    compra()
                else:
                    print("\nCompra cancelada")
                    print("\nVoltando ao menu da sua conta...\n")
                    menuloggedIn(loggedIn)
            else:
                print("\nDeseja fazer login para comprar algum livro destacado acima?\n")
                deseja = SimNao()
                if deseja == "S":
                    Login()
                else:
                    print("\nVoltando ao menu principal...\n")
                    main_menu()
        else:
            print(f"\nNenhum livro no estoque da livraria foi escrito por {Autor}")
            if loggedIn:
                print("\nVoltando ao menu da sua conta...\n")
                menuloggedIn(loggedIn)
            else:
                print("\nVoltando ao menu principal...\n")
                main_menu()
    else:
        while not (key_word.isnumeric()) or int(key_word) >= 10000 or int(key_word) <= 0:
            key_word = input("\nPor favor informe um número válido para o ano de publicação do livro:\n-> ")
        anoPublicacao = key_word
        if (ret := table_livro.read('titulo', ano_publicacao = anoPublicacao, search_type = 'ano_publicacao')):

            print(f"\nLivros publicados no ano de {anoPublicacao}:")
            i = 0
            for row in ret:
                i+=1
                print(f" {i} - {row[0]}")
            if loggedIn:
                print("\nDeseja comprar algum livro destacado acima?\n")
                comprar = SimNao()
                if comprar == "S":
                    compra()
                else:
                    print("\nCompra cancelada")
                    print("\nVoltando ao menu da sua conta...\n")
                    menuloggedIn(loggedIn)
            else:
                print("\nDeseja fazer login para comprar algum livro destacado acima?\n")
                deseja = SimNao()
                if deseja == "S":
                    Login()
                else:
                    print("\nVoltando ao menu principal...\n")
                    main_menu()
        else:
            print(f"\nNenhum livro no estoque da livraria foi publicado no ano de {anoPublicacao}")
            if loggedIn:
                print("\nVoltando ao menu da sua conta...\n")
                menuloggedIn(loggedIn)
            else:
                print("\nVoltando ao menu principal...\n")
                main_menu()
    quit()


def bookSearch(loggedIn):
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

    pesquisa(p, loggedIn)


def quitLibrary():
    print("\n\tFechando o sistema...")
    print("\n\tObrigado por visitar a livraria Tuko!\n")
    quit()

def verPedidos():
    print("\nAqui seus pedidos\n")
    pass

def menu(loggedIn):
    menu_c = ["L", "C", "P", "Q"]
    print("O que deseja fazer?")
    while True:
        choice = input( 
                "* (L) Realizar login \n"
                "* (C) Realizar cadastro \n"
                "* (P) Pesquisar livro \n"
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
        bookSearch(loggedIn)
    elif choice == "Q":
        quitLibrary()
    else:
        print("Deu ruim")
        exit(-666)


def menuloggedIn(loggedIn):

    print(f"\n\tOlá seja bem vindo de volta!\n")
    menu_c = ["C", "P", "S", "Q"]
    print("O que deseja fazer?")
    while True:
        choice = input(
                "* (C) Realizar compra\n"
                "* (P) Ver todos seus pedidos\n"
                "* (S) Sair da conta\n"
                "* (Q) Sair do sistema\n"
                "-> "
                )

        choice = choice.upper()

        if choice not in  menu_c:
            print("\nDesculpe, tente novamente...\n")
            continue
        else:
            break

    if choice   == "C":
        bookSearch(loggedIn)
    elif choice == "P":
        verPedidos()
    elif choice == "S":
        print("\nVoltando ao menu principal...\n")
        menu(loggedIn)
    elif choice == "Q":
        quitLibrary()
    else:
        print("Deu ruim")
        exit(-666)


def main_menu():
    loggedIn = False
    if loggedIn:
        menuloggedIn(loggedIn)
    else:
        menu(loggedIn)


def main():
    print("\n\t########################################################\n"
            "\t######## Olá seja bem vindo a livraria Tuko! ###########\n"
            "\t########################################################\n")
    main_menu()

if __name__ == "__main__":
    main()


# Testando o uso de dataFrames^^^^^^^^^^^^^
# def get_books():
#     for row in tables['livro'].read_all():
#         print(row)
#     print()

# def get_users():
#     for row in tables['cliente'].read_all():
#         print(row)
#     print()

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
