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
            sql = fmtSQL() \
                    .SELECT(select) \
                    .FROM('pedido')

            if search_type == "id":
                sql.WHERE('id_pedido = %s')
            elif search_type == "custo":
                sql.WHERE('custo = %s')
            data = self.query(sql, args)
            
            if data:
                return data
            
            return "Record not found in PedidoTable"
                
        except Exception as error:
            print("Record not found in PedidoTable", error)

    def read_all(self):
        try:
            sql = fmtSQL() \
                    .SELECT() \
                    .FROM('pedido')
            data = self.query(sql)
            
            if data:
                return data
            
            return "Record not found in PedidoTable"
        
        except Exception as error:
            print("Record not found in PedidoTable", error)

    # UPDATE
    def update(self, id, *args, update_type="custo"):
        try:
            sql = fmtSQL() \
                    .UPDATE('pedido')

            if update_type == "custo":
                sql.SET('name = %s')
            elif update_type == "email":
                sql.SET('email = %s')

            sql.WHERE(f'id_pedido = {id}')
            self.execute(sql, args)
            self.commit()
            print("Record updated")
            
        except Exception as error:
            print("Error updating pedido", error)

    #DELETE
    def delete(self, id):
        try:
            sql = fmtSQL() \
                    .FROM('pedido') \
                    .WHERE(f'id_pedido = {id}')
            sql_search = fmtSQL().SELECT() \
                            .append(sql)

            if not self.query(sql_search):
                return "Record not found on database"

            sql_delete = fmtSQL().DELETE() \
                            .append(sql)
                            
            self.execute(sql_delete)
            self.commit()
            
            return "Record deleted"
        
        except Exception as error:
            print("Error deleting record", error)
    
    # INSERT
    def insert(self, *args):
        try:
            sql = fmtSQL() \
                    .INSERT_INTO('pedido', '(name, email)') \
                    .VALUES('(%s, %s)')
            self.execute(sql, args)
            self.commit()
            
        except Exception as error:
            print("Error inserting record", error)
