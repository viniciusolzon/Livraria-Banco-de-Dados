from tabelas.config import Connection

# Herda de Connection pq vai utilizar os métodos de Connection
class LivroTable(Connection):
    # CREATE
    def __init__(self):
        Connection.__init__(self)
        # sql = """
        # CREATE TABLE IF NOT EXISTS livro(
        #     id_livro SERIAL PRIMARY KEY NOT NULL,
        #     preco FLOAT NOT NULL,
        #     titulo VARCHAR(255) NOT NULL,
        #     autor VARCHAR(255) NOT NULL,
        #     ano_publicacao INT NOT NULL
        # );
        # """
        # self.execute(sql)
        # self.commit()

    # READ/Search
    def read(self, select = '*', id_livro = 0, titulo = '', ano_publicacao = 0, autor = '', preco = 0.0, search_type = 'titulo'):
        try:
            sql = f"SELECT {select} FROM livro WHERE titulo = lower(unaccent('{titulo}'))"

            if search_type == "id_livro":
                sql = f"SELECT {select} FROM livro WHERE id_livro = {id_livro}"
            elif search_type == "ano_publicacao":
                sql = f"SELECT {select} FROM livro WHERE ano_publicacao = {ano_publicacao}"
            elif search_type == "autor":
                sql = f"SELECT {select} FROM livro WHERE autor = lower(unaccent('{autor}'))"
            elif search_type == "preco":
                sql = f"SELECT {select} FROM livro WHERE preco = {preco}"

            data = self.query(sql)

            if data:
                return data
            
            return False
        except Exception as error:
            print("Record not found in LivroTable", error)
            

    def read_all(self, select = '*'):
        try:
            sql = f"SELECT {select} FROM livro"

            data = self.query(sql)
            if data:
                return data
            
            return False
        except Exception as error:
            print("Record not found in LivroTable", error)

    # UPDATE
    def update(self, id_livro=0, titulo = '', ano_publicacao = 0, autor = '', preco = 0.0, update_type = 'titulo'):
        try:
            sql = f"UPDATE livro SET preco = {preco} WHERE id_livro = {id_livro}"

            if update_type == "ano_publicacao":
                sql = f"UPDATE livro SET ano_publicacao = {ano_publicacao} WHERE id_livro = {id_livro}"
            elif update_type == "autor":
                sql = f"UPDATE livro SET autor = lower(unaccent('{autor}')) WHERE id_livro = {id_livro}"
            elif update_type == "preco":
                sql = f"UPDATE livro SET preco = {preco} WHERE id_livro = {id_livro}"
            elif update_type == "titulo":
                sql = f"UPDATE livro SET titulo = lower(unaccent('{titulo}')) WHERE id_livro = {id_livro}"
                
            self.execute(sql)
            self.commit()
            # print("Record updated")
        except Exception as error:
            print("Error updating livro", error)

    # INSERT
    def insert(self, titulo = '', autor = '', ano_publicacao = 0, preco = 0.0):
        try:
            sql = f"INSERT INTO livro (titulo, autor, ano_publicacao, preco) VALUES (lower(unaccent('{titulo}')), lower(unaccent('{autor}')), {ano_publicacao}, {preco})"

            self.execute(sql)
            self.commit()
        except Exception as error:
            print("Error inserting record", error)

    # DELETE
    def delete(self, id_livro = 0):
        try:
            sql_search = f"SELECT * FROM livro WHERE id_livro = {id_livro}"

            if not self.query(sql_search):
                return "Record not found on database"
            sql_delete = f"DELETE FROM livro WHERE id_livro = {id_livro}"

            self.execute(sql_delete)
            self.commit()

            return True
        except Exception as error:
            print("Error deleting record", error)

# Testando
# tables = {}
# tables['livros'] = LivroTable()
# print(tables['livros'].read('titulo', preco = 69.99, search_type='preco'))
# print(tables['livros'].read('autor', preco = 69.99, search_type='preco'))
# print(tables['livros'].read('ano_publicacao', preco = 69.99, search_type='preco'))

# print(tables['livros'].read('preco', titulo = 'Contos De Voltaire', search_type='titulo'))
# print(tables['livros'].read('autor', titulo = 'Contos De Voltaire', search_type='titulo'))
# print(tables['livros'].read('ano_publicacao', titulo = 'Contos De Voltaire', search_type='titulo'))

# print(tables['livros'].read('titulo', ano_publicacao = 1890, search_type='ano_publicacao'))
# print(tables['livros'].read('preco', ano_publicacao = 1890, search_type='ano_publicacao'))
# print(tables['livros'].read('autor', ano_publicacao = 1890, search_type='ano_publicacao'))

# print(tables['livros'].read('ano_publicacao', autor = 'William Golding', search_type='autor'))
# print(tables['livros'].read('titulo', autor = 'William Golding', search_type='autor'))
# print(tables['livros'].read('preco', autor = 'William Golding', search_type='autor'))

# tables['livros'].update(id_livro=1, ano_publicacao= 2008, update_type = 'ano_publicacao')
# tables['livros'].update(id_livro=1, preco = 120.00, update_type = 'preco')
# tables['livros'].update(id_livro=1, titulo = 'Codigo Limpo', update_type = 'titulo')
# tables['livros'].update(id_livro=1, autor = 'Robert Cecil Martin', update_type = 'autor')

# tables['livros'].insert("Codigo Limpo", "Robert Cecil Martin", 2008, 69.99)

# tables['livros'].delete(id_livro = 7)
