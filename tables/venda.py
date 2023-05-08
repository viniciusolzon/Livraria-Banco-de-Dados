from config import Connection
from fmt_sql import fmtSQL

# Herda de Connection pq vai utilizar os métodos de Connection
class VendaTable(Connection):
    # CREATE
    def __init__(self):
        Connection.__init__(self)
        # Pra não ter que ficar toda hora indo no pgAdmin4 e deletando a tabela manualmente pra executar os comandos sem problema
        # self.execute("DROP TABLE IF EXISTS venda")
        # Cria a tabela se ela ainda não existe
        sql = """
        CREATE TABLE IF NOT EXISTS venda(
            id_pedido SERIAL PRIMARY KEY,
            custo_total FLOAT,
            id_cliente INT,
            FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente)
        );
        """
        self.execute(sql)
        self.commit()

    #READ/Search
    def read(self, *args, search_type="id"): # A busca padrão é pelo id
        try:
            sql = fmtSQL() \
                    .SELECT() \
                    .FROM('venda')

            if search_type == "id":
                #sql = "SELECT * FROM venda WHERE id = %s"
                sql.WHERE('id = %s')
            # Porém o usuário tbm pode querer pesquisar pelo nome
            elif search_type == "nome":
                #sql = "SELECT * FROM venda WHERE nome = %s"
                sql.WHERE('nome = %s')
            data = self.query(sql, args)
            if data:
                return data
            return "Record not found in VendaTable"
                
        except Exception as error:
            print("Record not found in VendaTable", error)

    def read_all(self):
        try:
            #sql = "SELECT * FROM venda"
            sql = fmtSQL() \
                    .SELECT() \
                    .FROM('venda')
            data = self.query(sql)
            if data:
                return data
            return "Record not found in VendaTable"
        except Exception as error:
            print("Record not found in VendaTable", error)

    # UPDATE
    def update(self, id, *args, update_type="nome"):
        try:
            #sql = f"UPDATE venda SET name = %s WHERE id = {id}"
            sql = fmtSQL() \
                    .UPDATE('venda')

            if update_type == "nome":
                sql.SET('name = %s')
            elif update_type == "email":
                #sql = f"UPDATE venda SET email = %s WHERE id = {id}"
                sql.SET('email = %s')

            sql.WHERE(f'id = {id}')
            self.execute(sql, args)
            self.commit()
            print("Record updated")
        except Exception as error:
            print("Error updating venda", error)

    #DELETE
    def delete(self, id):
        try:
            sql = fmtSQL() \
                    .FROM('venda') \
                    .WHERE(f'id = {id}')
            # Busca no banco de dados pra ver se existe
            #sql_search = f"SELECT * FROM venda WHERE id = {id}"
            sql_search = fmtSQL().SELECT() \
                            .append(sql)

            if not self.query(sql_search):
                return "Record not found on database"
            # Deleta
            #sql_delete = f"DELETE FROM venda WHERE id = {id}"
            sql_search = fmtSQL().DELETE() \
                            .append(sql)
                            
            self.execute(sql_delete)
            self.commit()
            return "Record deleted"
        except Exception as error:
            print("Error deleting record", error)
    
    # INSERT
    def insert(self, *args):
        try:
            #sql = f"INSERT INTO venda (name, email) VALUES (%s, %s)"
            sql = fmtSQL() \
                    .INSERT_INTO('venda', '(name, email)') \
                    .VALUES('(%s, %s)')
            self.execute(sql, args)
            self.commit()
        except Exception as error:
            print("Error inserting record", error)

