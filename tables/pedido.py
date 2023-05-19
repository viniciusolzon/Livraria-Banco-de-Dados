from config import Connection

# Herda de Connection pq vai utilizar os métodos de Connection
class PedidoTable(Connection):
    # CREATE
    def __init__(self):
        Connection.__init__(self)
        sql = """
        CREATE TABLE IF NOT EXISTS pedido(
            id_pedido SERIAL PRIMARY KEY,
            custo FLOAT,
            id_cliente INT,
            id_livro INT,
            FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente),
            FOREIGN KEY (id_livro) REFERENCES livro (id_livro)
        );
        """
        self.execute(sql)
        self.commit()

    #READ/Search
    def read(self, *args, select = '*', search_type="id"):
        try:
            sql = 'SELECT id_pedido FROM pedido'

            if search_type == "custo":
                sql = 'SELECT custo FROM pedido WHERE id_cliente = "%s"'
            elif search_type == "id_cliente":
                sql = 'SELECT id_cliente FROM pedido WHERE id_cliente = "%s'
            elif search_type == "id_livro":
                sql = 'SELECT id_livro FROM pedido WHERE id_cliente = "%s'

            data = self.query(sql, args)[0][0]
            if data:
                return data
            
            return "Record not found in PedidoTable"
                
        except Exception as error:
            print("Record not found in PedidoTable", error)

    def read_all(self):
        try:
            sql = 'SELECT * FROM PEDIDO'

            data = self.query(sql)[0][0]
            if data:
                return data
            
            return "Record not found in PedidoTable"
        
        except Exception as error:
            print("Record not found in PedidoTable", error)

    # UPDATE
    def update(self, id, discount, search_type = 'id_pedido'):
        try:
            sql = f'UPDATE pedido SET custo = custo * {discount} WHERE id_pedido = {id}' # desconto em um pedido
            
            if search_type == 'id_cliente':        
                sql = f'UPDATE pedido SET custo = custo * {discount} WHERE id_cliente = {id}' # desconto em todos pedidos do cliente


            self.execute(sql)
            self.commit()
            print("Record updated")
            
        except Exception as error:
            print("Error updating pedido", error)

    # DELETE
    def delete(self, *args):
        try:
            
            sql_search = "SELECT * FROM pedido WHERE id_pedido = '%s'"

            if not self.query(sql_search):
                return "Record not found on database"
            
            sql_delete = 'DELETE * FROM pedido WHERE id_pedido = "%s"'
            self.execute(sql_delete, args)
            self.commit()
            
        except Exception as error:
            print("Error deleting record", error)
