from config import Connection

# Herda de Connection pq vai utilizar os métodos de Connection
class LivroTable(Connection):
    # CREATE
    def __init__(self):
        Connection.__init__(self)
        sql = """
        CREATE TABLE IF NOT EXISTS livro(
            id_livro SERIAL PRIMARY KEY,
            preco FLOAT,
            titulo VARCHAR(255),
            genero VARCHAR(255),
            autor VARCHAR(255),
            ano_publicacao INT
        );
        """
        self.execute(sql)
        self.commit()

    # READ/Search
    def read(self, select, titulo, id_livro = '', ano_publicacao = '', genero = '', autor = '', preco = '', search_type = 'titulo'):
        try:
            sql = f"SELECT {select} FROM livro WHERE titulo = '{titulo}'"
            
            if search_type == "id":
                sql = f"SELECT {select} FROM livro WHERE id_livro = {id_livro}"
            elif search_type == "ano_publicacao":
                sql = f"SELECT {select} FROM livro WHERE ano_publicacao = {ano_publicacao}"
            elif search_type == "genero":
                sql = f"SELECT {select} FROM livro WHERE genero = {genero}"
            elif search_type == "autor":
                sql = f"SELECT {select} FROM livro WHERE autor = {autor}"
            elif search_type == "preco":
                sql = f"SELECT {select} FROM livro WHERE preco = {preco}"

            data = self.query(sql)[0][0]
            if data:
                return data
            
            return False
        except Exception as error:
            print("Record not found in LivroTable", error)

    def read_all(self):
        try:
            sql = "SELECT * FROM livro WHERE id_livro = "

            data = self.query(sql)[0][0]
            if data:
                return data
            return False
        except Exception as error:
            print("Record not found in LivroTable", error)

    # UPDATE
    def update(self, id, preco, titulo, genero, autor, ano_publicacao):
        try:
            sql = f"UPDATE livro SET preco = %s, titulo = %s, genero = %s, autor = %s, ano_publicacao = %s WHERE id = {id}"
                    
            self.execute(sql)
            self.commit()
            # print("Record updated")
        except Exception as error:
            print("Error updating livro", error)

    # INSERT
    def insert(self, preco, titulo, genero, autor, ano_publicacao):
        try:
            sql = f"INSERT INTO livro (preco, titulo, genero, autor, ano_publicacao) VALUES ({preco}, {titulo}, {genero}, {autor}, {ano_publicacao})"

            self.execute(sql)
            self.commit()
        except Exception as error:
            print("Error inserting record", error)

    # DELETE
    def delete(self, id):
        try:
            sql_search = f"SELECT * FROM livro WHERE id = {id}"

            if not self.query(sql_search):
                return "Record not found on database"
            sql_delete = f"DELETE FROM livro WHERE id = {id}"

            self.execute(sql_delete)
            self.commit()

            return True
        except Exception as error:
            print("Error deleting record", error)

tables = {}
tables['livros'] = LivroTable()
print(tables['livros'].read('preco', 'Contos De Voltaire'))
