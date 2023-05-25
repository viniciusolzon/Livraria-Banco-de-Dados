from tabelas.config import Connection

# Herda de Connection pq vai utilizar os métodos de Connection
class PedidoTable(Connection):
    # CREATE
    def __init__(self):
        Connection.__init__(self)
        sql = """
        CREATE TABLE IF NOT EXISTS pedido(
            id_pedido SERIAL PRIMARY KEY NOT NULL, 
            custo FLOAT NOT NULL,
            usuario VARCHAR(50) NOT NULL,

            FOREIGN KEY (usuario) REFERENCES cliente (usuario)
        );
        """
            #PRIMARY KEY (id_pedido),
        self.execute(sql)
        self.commit()

        self.columns = ['id_pedido', 'custo', 'usuario']

    def getCols(self):
        return self.columns

    #READ/Search
    def read(self, usuario, select = '*', id_pedido = 0, id_livro = 0, custo = 0, search_type = "usuario"):
        try:
            sql = f"SELECT {select} FROM pedido WHERE usuario = '{usuario}'"

            if search_type == "id_pedido":
                sql = f'SELECT {select} FROM pedido WHERE id_pedido = {id_pedido}'
            elif search_type == "id_livro":
                sql = f'SELECT {select} FROM pedido WHERE id_livro = {id_livro}'
            elif search_type == "custo":
                sql = f'SELECT {select} FROM pedido WHERE custo = {custo}'

            data = self.query(sql)
            if data:
                return data
            
            return False
        except Exception as error:
            print("Record not found in PedidoTable", error)

    def read_all(self, select = '*'):
        try:
            sql = f'SELECT {select} FROM pedido'

            data = self.query(sql)
            if data:
                return data
            
            return False
        except Exception as error:
            print("Record not found in PedidoTable", error)

    # UPDATE
    def update(self, id_pedido, usuario = None, custo = None, update_type = 'custo'):
        try:
            #sql = f'UPDATE pedido SET custo = custo * {1 - desconto} WHERE id_pedido = {id_pedido}' # desconto por pedido

            if update_type == 'usuario':
                sql = f"UPDATE pedido SET usuario = '{usuario}' WHERE id_pedido = {id_pedido}"
            elif update_type == 'custo':
                sql = f"UPDATE pedido SET custo = {custo} WHERE id_pedido = {id_pedido}" # desconto por cliente
            else:
                print("lascou")

            self.execute(sql)
            self.commit()
            # print("Record updated")
        except Exception as error:
            print("Error updating pedido", error)

    # INSERT
    def insert(self, usuario, custo):
        try:
            sql = f"INSERT INTO pedido (usuario, custo) VALUES ('{usuario}', {custo}); SELECT CURRVAL('pedido_id_pedido_seq');"

            self.execute(sql)
            self.commit()
            return self.fetchall()[0][0]
        except Exception as error:
            print("Error inserting record", error)

    # DELETE
    def delete(self, id_pedido):
        try:
            sql_search = f"SELECT * FROM pedido WHERE id_pedido = {id_pedido}"

            if not self.query(sql_search):
                return "Record not found on database"
            
            sql_delete = f"DELETE FROM pedido WHERE id_pedido = {id_pedido}"
            self.execute(sql_delete)
            self.commit()
            
        except Exception as error:
            print("Error deleting record", error)
