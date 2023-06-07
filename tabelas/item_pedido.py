from tabelas.config import Connection

# Herda de Connection pq vai utilizar os métodos de Connection
class ItemPedidoTable(Connection):
    # CREATE
    def __init__(self):
        Connection.__init__(self)
        sql = """
        CREATE TABLE IF NOT EXISTS item_pedido(
            id_item_pedido SERIAL PRIMARY KEY NOT NULL,
            id_pedido INT NOT NULL,
            id_livro INT NOT NULL,
            FOREIGN KEY (id_pedido) REFERENCES pedido (id_pedido),
            FOREIGN KEY (id_livro) REFERENCES livro (id_livro)
        );
        """
        self.execute(sql)
        self.commit()

    #READ/Search
    def read(self, select = '*', id_pedido = 0, id_item_pedido = 0, id_livro = 0, search_type = "id_pedido"):
        try:
            sql = f'SELECT {select} FROM item_pedido WHERE id_pedido = {id_pedido}'

            if search_type == "id_item_pedido":
                sql = f'SELECT {select} FROM item_pedido WHERE id_item_pedido = {id_item_pedido}'
            elif search_type == "id_livro":
                sql = f'SELECT {select} FROM item_pedido WHERE id_livro = {id_livro}'

            data = self.query(sql)
            if data:
                return data
            
            return False
        except Exception as error:
            print("Record not found in ItemPedidoTable", error)

    def read_all(self, select = '*'):
        try:
            sql = f'SELECT {select} FROM item_pedido'

            data = self.query(sql)
            if data:
                return data
            
            return False
        except Exception as error:
            print("Record not found in ItemTable", error)

    # INSERT
    def insert(self, id_pedido = 0, id_livro = 0):
        try:
            sql = f"INSERT INTO item_pedido (id_pedido, id_livro) VALUES ({id_pedido}, {id_livro})"

            self.execute(sql)
            self.commit()
        except Exception as error:
            print("Error inserting record", error)

    # DELETE
    def delete(self, id_pedido = 0):
        try:
            sql_search = f"SELECT * FROM item_pedido WHERE id_pedido = {id_pedido}"

            if not self.query(sql_search):
                return "Record not found on database"
            
            
            sql_delete = f"DELETE FROM item_pedido WHERE id_pedido = {id_pedido}"
            
            self.execute(sql_delete)
            self.commit()
            
        except Exception as error:
            print("Error deleting record", error)
