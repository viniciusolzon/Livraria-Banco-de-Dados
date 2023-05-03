from config import Connection

# Herda de Connection pq vai utilizar os métodos de Connection
class LivroTable(Connection):
    # CREATE
    def __init__(self):
        Connection.__init__(self)
        # Pra não ter que ficar toda hora indo no pgAdmin4 e deletando a tabela manualmente pra executar os comandos sem problema
        self.execute("DROP TABLE IF EXISTS livro")
        # Cria a tabela se ela ainda não existe
        sql = """
        CREATE TABLE IF NOT EXISTS livro(
            id SERIAL PRIMARY KEY,
            titulo VARCHAR(255),
            genero VARCHAR(255),
            autor VARCHAR(255),
            ano_publicacao INT;
        );
        """
        self.execute(sql)

    #READ/Search
    def read(self, *args, search_type="id"): # A busca padrão é pelo nome
        try:
            sql = "SELECT * FROM livro WHERE id = %s"
            # Porém o usuário tbm pode querer pesquisar pelo id
            if search_type == "titulo":
                sql = "SELECT * FROM livro WHERE titulo = %s"
            data = self.query(sql, args)
            if data:
                return data
            return "Record not found in LivroTable"
        except Exception as error:
            print("Record not found in LivroTable", error)

    def read_all(self):
        try:
            sql = "SELECT * FROM livro;"
            data = self.query(sql)
            if data:
                return data
            return "Record not found in LivroTable"
        except Exception as error:
            print("Record not found in LivroTable", error)

    # UPDATE
    def update(self, id, *args):
        try:
            sql = f"UPDATE livro SET titulo = %s, genero = %s, autor = %s, ano_publicacao = %s WHERE id = {id}"
            self.execute(sql, args)
            self.commit()
            print("Record updated")
        except Exception as error:
            print("Error updating livro", error)

    #DELETE
    def delete(self, id):
        try:
            # Busca no banco de dados pra ver se existe
            sql_search = f"SELECT * FROM livro WHERE id = {id}"
            if not self.query(sql_search):
                return "Record not found on database"
            # Deleta
            sql_delete = f"DELETE FROM livro WHERE id = {id}"
            self.execute(sql_delete)
            self.commit()
            return "Record deleted"
        except Exception as error:
            print("Error deleting record", error)
    
    # INSERT
    def insert(self, *args):
        try:
            sql = f"INSERT INTO livro (titulo, genero, autor, ano_publicacao) VALUES (%s, %s, %s, %s)"
            self.execute(sql, args)
            self.commit()
        except Exception as error:
            print("Error inserting record", error)
