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
            id_livro INT NOT NULL,
            custo_total FLOAT NOT NULL,
            FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente),
            FOREIGN KEY (id_livro) REFERENCES livro (id_livro)
        );
        """
        self.execute(sql)
        self.commit()

    #READ/Search
    def read(self, select = '*', id_carrinho = 0, id_cliente = 0, id_livro = 0, custo_total = 0, search_type = "id_cliente"):
        try:
            sql = f'SELECT {select} FROM carrinho WHERE id_cliente = {id_cliente}'

            if search_type == "id_carrinho":
                sql = f'SELECT {select} FROM carrinho WHERE id_carrinho = {id_carrinho}'
            elif search_type == "id_livro":
                sql = f'SELECT {select} FROM carrinho WHERE id_livro = {id_livro}'
            elif search_type == "custo_total":
                sql = f'SELECT {select} FROM carrinho WHERE custo_total = {custo_total}'

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

    # UPDATE
    def update(self, desconto = 0.0, id_carrinho = 0, id_cliente = 0, update_type = 'id_carrinho'):
        try:
            sql = f'UPDATE carrinho SET custo_total = custo_total * {1 - desconto} WHERE id_carrinho = {id_carrinho}' # desconto por carrinho

            if update_type == 'id_cliente':
                sql = f'UPDATE carrinho SET custo_total = custo_total * {1 - desconto} WHERE id_cliente = {id_cliente}' # desconto por cliente

            self.execute(sql)
            self.commit()
            # print("Record updated")
        except Exception as error:
            print("Error updating carrinho", error)

    # INSERT
    def insert(self, id_cliente = 0, id_livro = 0, custo_total = 0):
        try:
            sql = f"INSERT INTO carrinho (id_cliente, id_livro, custo_total) VALUES ({id_cliente}, {id_livro}, {custo_total})"

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
