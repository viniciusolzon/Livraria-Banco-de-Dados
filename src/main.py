from initializer import tables
import pandas as pd

from sqlalchemy import create_engine


def get_users():
    for row in tables['cliente'].read_all():
        print(row)
    print()

def get_books():
    for row in tables['livro'].read_all():
        print(row)
    print()


def main():

    # Create an engine instance
    alchemyEngine   = create_engine('postgresql+psycopg2://postgres:1234@localhost:5432')
    # Connect to PostgreSQL server
    dbConnection    = alchemyEngine.connect()
    # Create a dataframe
    dataFrame = pd.read_sql_query("SELECT * FROM livro;", dbConnection)

    print(dataFrame.head(10))
    
    # get_books()
    # get_users()



if __name__ == "__main__":
    main()
