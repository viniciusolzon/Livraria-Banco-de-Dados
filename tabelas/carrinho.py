from tabelas.config import Connection

# Herda de Connection pq vai utilizar os métodos de Connection
class CarrinhoTable(Connection):
    # CREATE
    def __init__(self):
        Connection.__init__(self)
        sql = """
        CREATE TABLE IF NOT EXISTS carrinho(
            id_carrinho SERIAL PRIMARY KEY NOT NULL,
            id_cliente INT NOT NULL,
            FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente)
        );
        """
        self.execute(sql)
        self.commit()

    #READ/Search
    def read(self, select = '*', id_carrinho = 0, id_cliente = 0, search_type = "id_cliente"):
        try:
            sql = f'SELECT {select} FROM carrinho WHERE id_cliente = {id_cliente}'

            if search_type == "id_carrinho":
                sql = f'SELECT {select} FROM carrinho WHERE id_carrinho = {id_carrinho}'

            data = self.query(sql)
            if data:
                return data
            
            return False
        except Exception as error:
            print("Record not found in CarrinhoTable", error)

    def read_all(self, select = '*'):
        try:
            sql = f'SELECT {select} FROM carrinho'

            data = self.query(sql)
            if data:
                return data
            
            return False
        except Exception as error:
            print("Record not found in CarrinhoTable", error)

    # INSERT
    def insert(self, id_cliente = 0):
        try:
            sql = f"INSERT INTO carrinho (id_cliente) VALUES ({id_cliente})"

            self.execute(sql)
            self.commit()
        except Exception as error:
            print("Error inserting record", error)

    # DELETE
    def delete(self, id_carrinho = 0):
        try:
            sql_search = f"SELECT * FROM carrinho WHERE id_carrinho = {id_carrinho}"

            if not self.query(sql_search):
                return "Record not found on database"
            
            sql_delete = f"DELETE FROM carrinho WHERE id_carrinho = {id_carrinho}"
            self.execute(sql_delete)
            self.commit()
            
        except Exception as error:
            print("Error deleting record", error)
