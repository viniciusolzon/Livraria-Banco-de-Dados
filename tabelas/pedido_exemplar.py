from tabelas.config import Connection

# Herda de Connection pq vai utilizar os métodos de Connection
class PedidoExemplarTable(Connection):
    # CREATE
    def __init__(self):
        Connection.__init__(self)
        sql = """
        CREATE TABLE IF NOT EXISTS pedido_exemplar(
            id_exemplar INT NOT NULL,
            id_pedido INT NOT NULL,
            PRIMARY KEY (id_exemplar, id_pedido)
        );
        """
            #PRIMARY KEY (id_exemplar),
        self.execute(sql)
        self.commit()
        
        self.columns = ['id_exemplar', 'id_pedido']

    def getCols(self):
        return self.columns

    # READ/Search
    def read(self, id_exemplar, id_pedido, search_type = 'id_exemplar'):
        try:
            sql = f'SELECT * FROM pedido_exemplar WHERE id_exemplar = {id_exemplar};'
            if search_type == 'id_pedido':
                sql = f'SELECT * FROM pedido_exemplar WHERE id_pedido = {id_pedido};'

            data = self.query(sql)
            if data:
                return data
            
            return False
        except Exception as error:
            print("Record not found in EstoqueTable", error)

    def read_all(self, select = "*"):
        try:
            sql = f'SELECT {select} FROM pedido_exemplar;'
            
            data = self.query(sql)
            if data:
                return data

            return False
        except Exception as error:
            print("Record not found in EstoqueTable", error)

    # INSERT
    def insert(self, id_pedido, id_exemplar):
        try:
            sql = f"INSERT INTO pedido_exemplar (id_pedido, id_exemplar) VALUES ({id_pedido}, {id_exemplar})"

            self.execute(sql)
            self.commit()
        except Exception as error:
            print("Error inserting record", error)

    # DELETE
    def delete(self, id_pedido, id_exemplar):
        try:
            sql_search = f"SELECT * FROM pedido_exemplar WHERE id_pedido = {id_pedido} AND id_exemplar = {id_exemplar};"

            if not self.query(sql_search):
                return "Record not found on database"
            
            sql_delete = f'DELETE FROM pedido_exemplar WHERE id_pedido = {id_pedido} AND id_exemplar = {id_exemplar}'
            self.execute(sql_delete)
            self.commit()
            
        except Exception as error:
            print("Error deleting record", error)

