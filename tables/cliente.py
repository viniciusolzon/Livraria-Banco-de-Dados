from config import Connection
from fmt_sql import fmtSQL

# Herda de Connection pq vai utilizar os métodos de Connection
class ClienteTable(Connection):
    # CREATE
    def __init__(self):
        Connection.__init__(self)
        # Pra não ter que ficar toda hora indo no pgAdmin4 e deletando a tabela manualmente pra executar os comandos sem problema
        # self.execute("DROP TABLE IF EXISTS cliente")
        # Cria a tabela se ela ainda não existe
        sql = """
        CREATE TABLE IF NOT EXISTS cliente(
            id_cliente SERIAL PRIMARY KEY,
            nome VARCHAR(255),
            usuario VARCHAR(255),
            senha VARCHAR(255),
            email VARCHAR(255)
        );
        """
        self.execute(sql)
        self.commit()

    #READ/Search
    def read(self, *args, select = '*', search_type="id"): # A busca padrão é pelo id
        try:
            sql = fmtSQL() \
                    .SELECT(select) \
                    .FROM('cliente')

            # Outros tipos de pesquisa
            if search_type == "nome":
                #sql = "SELECT * FROM cliente WHERE nome = %s"
                sql.WHERE('nome = %s')
            elif search_type == "email":
                #sql = "SELECT * FROM cliente WHERE email = %s"
                sql.WHERE('email = %s')
            elif search_type ==  "usuario":
                #sql = "SELECT * FROM cliente WHERE usuario = %s"
                sql.WHERE('usuario = %s')
            elif search_type ==  "senha":
                #sql = "SELECT senha FROM cliente WHERE usuario = %s"
                sql = fmtSQL() \
                        .SELECT('senha') \
                        .FROM('cliente') \
                        .WHERE('usuario = %s')
            else:
                #sql = "SELECT * FROM cliente WHERE id_cliente = %s"
                sql.WHERE('id_cliente = %s')

            data = self.query(sql, args)
            if data:
                return data
            return False # "Record not found in ClienteTable"
                
        except Exception as error:
            print("Record not found in ClienteTable", error)

    def read_all(self):
        try:
            #sql = "SELECT * FROM cliente"
            sql = fmtSQL() \
                    .SELECT() \
                    .FROM('cliente')

            data = self.query(sql)
            if data:
                return data
            return False # "Record not found in ClienteTable"
        except Exception as error:
            print("Record not found in ClienteTable", error)

    # UPDATE
    def update(self, id, *args, update_type="nome"):
        try:
            #sql = f"UPDATE cliente SET nome = %s WHERE id = {id}"
            sql = fmtSQL() \
                    .UPDATE('cliente')
            if update_type == "nome":
                sql.SET('nome = %s') \
                    .WHERE(f'id_cliente = {id}')
            elif update_type == "email":
                sql.SET('email = %s') \
                    .WHERE(f'id = {id}')
                #sql = f"UPDATE cliente SET email = %s WHERE id = {id}"

            self.execute(sql, args)
            self.commit()
            print("Record updated")
        except Exception as error:
            print("Error updating cliente", error)

    #DELETE
    def delete(self, id):
        try:
            # Busca no banco de dados pra ver se existe
            #sql_search = f"SELECT * FROM cliente WHERE id = {id}"
            sql_search = fmtSQL() \
                    .SELECT() \
                    .FROM('cliente') \
                    .WHERE(f'id_cliente = {id}')

            if not self.query(sql_search):
                return False # "Record not found on database"
            # Deleta
            #sql_delete = f"DELETE FROM cliente WHERE id = {id}"
            sql_delete = fmtSQL() \
                    .DELETE() \
                    .FROM('cliente') \
                    .WHERE(f'id_cliente = {id}')

            self.execute(sql_delete)
            self.commit()
            return False # "Record deleted"
        except Exception as error:
            print("Error deleting record", error)
    
    # INSERT
    def insert(self, *args):
        try:
            #sql = f"INSERT INTO cliente (nome, usuario, senha, email) VALUES (%s, %s, %s, %s)"
            sql = fmtSQL() \
                    .INSERT_INTO('cliente', '(nome, usuario, senha, email)') \
                    .VALUES(f'(%s, %s, %s, %s)')
            self.execute(sql, args)
            self.commit()
        except Exception as error:
            print("Error inserting record", error)
