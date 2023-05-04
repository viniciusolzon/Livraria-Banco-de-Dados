from initializer import tables
from sqlalchemy import create_engine
import pandas as pd
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu(choice):
    choice = input("Olá seja bem vindo a livraria 'Nome'! O que deseja fazer?\n* Realizar login (L)\n* Realizar cadastro (C)\n* Pesquisar livro sem cadastro (P)\n-> ")
    while(choice.upper() != "L" and choice.upper() != "C" and choice.upper() != "P"):
        choice = input("\nDesculpe, tente novamente...\n\n* Realizar login (L)\n* Realizar cadastro (C)\n* Pesquisar livro sem cadastro (P)\n-> ")
    return choice

def checkLogin(choice):
    if choice.upper() == "L":
        username = input("\tNome de usuário: ")
        # checa se o nome de usuário existe na tabela "cliente", se não existe a gente já para aqui e fala: "O usuário digitado não foi encontrado no registro"
        # se existe só continua pra próxima etapa pra verificar a senha
        password = input("\tSenha: ")
        # checa se a senha existe na tabela "cliente", se não existe a gente já para aqui e fala: "A senha digitada não coincide com o usuário em questão"
        # se digitada corretamente, libera o login
        loggedIn()

def checkRegister(choice):
    print()

def loggedIn():
    print("Login realizado com sucesso.\nBem vindo de volta 'nome'!\n ")


def main_menu():
    choice = menu(choice)
    
    if choice.upper() == "L":
        username = input("\tNome de usuário: ")
        # checa se o nome de usuário existe na tabela "cliente", se não existe a gente já para aqui e fala: "O usuário digitado não foi encontrado no registro"
        # se existe só continua pra próxima etapa pra verificar a senha
        password = input("\tSenha: ")
        # checa se a senha existe na tabela "cliente", se não existe a gente já para aqui e fala: "A senha digitada não coincide com o usuário em questão"
        # se digitada corretamente, libera o login
        loggedIn()
    
    elif choice.upper() == "C":
        nome = input("\tNome completo: ")
        # checa se o nome existe na tabela "cliente", se existe fala "O nome inserido já possui cadastro na livraria"
        email = input("\tEmail: ")
        # checa se o nome existe na tabela "cliente", se existe fala "O nome inserido já possui cadastro na livraria"
        email = input("\tNome de usuário: ")
        # checa 
        email = input("\tSenha: ")
        # checa 
        
        print("Cadastro realizado!")
    
    elif choice.upper() == "P":
        pesquisa = input("\nAqui você consegue consultar os livros contidos no estoque da nossa livraria:\n* Pesquisa por título (T)\n* Pesquisa por autor (A)\n* Pesquisa por ano de publicação (P)\n-> ")
        while(pesquisa.upper() != "T" and pesquisa.upper() != "A" and pesquisa.upper() != "P"):
            pesquisa = input("\nDesculpe, tente novamente...\n\n Pesquisa por título (T)\n* Pesquisa por autor (A)\n* Pesquisa por ano de publicação (P)\n-> ")


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
    dataFrame = pd.read_sql_query("SELECT * FROM usuario;", dbConnection)

    print(dataFrame.head())
    
    # get_books()
    # get_users()


if __name__ == "__main__":
    # main()
    main_menu()
