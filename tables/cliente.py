from config import Connection

# Herda de Connection pq vai utilizar os métodos de Connection
class ClienteTable(Connection):
    # CREATE
    def __init__(self):
        Connection.__init__(self)
        # Pra não ter que ficar toda hora indo no pgAdmin4 e deletando a tabela manualmente pra executar os comandos sem problema
        self.execute("DROP TABLE IF EXISTS cliente")
        # Cria a tabela se ela ainda não existe
        sql = """
        CREATE TABLE IF NOT EXISTS cliente(
            id_cliente SERIAL PRIMARY KEY,
            name VARCHAR(255),
            username VARCHAR(255),
            password VARCHAR(255),
            email TEXT
        );
        """
        self.execute(sql)

    #READ/Search
    def read(self, *args, search_type="id"): # A busca padrão é pelo id
        try:
            sql = "SELECT * FROM cliente WHERE id = %s"
            # Porém o usuário tbm pode querer pesquisar pelo nome
            if search_type == "nome":
                sql = "SELECT * FROM cliente WHERE nome = %s"
            data = self.query(sql, args)
            if data:
                for row in data:
                    print
                return data
            return "Record not found in ClienteTable"
                
        except Exception as error:
            print("Record not found in ClienteTable", error)

    def read_all(self):
        try:
            sql = "SELECT * FROM cliente"
            data = self.query(sql)
            if data:
                return data
            return "Record not found in ClienteTable"
        except Exception as error:
            print("Record not found in ClienteTable", error)

    # UPDATE
    def update(self, id, *args, update_type="nome"):
        try:
            sql = f"UPDATE cliente SET name = %s WHERE id = {id}"
            if update_type == "email":
                sql = f"UPDATE cliente SET email = %s WHERE id = {id}"
            self.execute(sql, args)
            self.commit()
            print("Record updated")
        except Exception as error:
            print("Error updating cliente", error)

    #DELETE
    def delete(self, id):
        try:
            # Busca no banco de dados pra ver se existe
            sql_search = f"SELECT * FROM cliente WHERE id = {id}"
            if not self.query(sql_search):
                return "Record not found on database"
            # Deleta
            sql_delete = f"DELETE FROM cliente WHERE id = {id}"
            self.execute(sql_delete)
            self.commit()
            return "Record deleted"
        except Exception as error:
            print("Error deleting record", error)
    
    # INSERT
    def insert(self, *args):
        try:
            sql = f"INSERT INTO cliente (name, username, password, email) VALUES (%s, %s, %s, %s)"
            self.execute(sql, args)
            self.commit()
        except Exception as error:
            print("Error inserting record", error)

