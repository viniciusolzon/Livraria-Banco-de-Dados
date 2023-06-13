from tabelas.config import Connection

# Herda de Connection pq vai utilizar os métodos de Connection
class ItemCarrinhoTable(Connection):
    # CREATE
    def __init__(self):
        Connection.__init__(self)
        # sql = """
        # CREATE TABLE IF NOT EXISTS item_carrinho(
        #     id_item_carrinho SERIAL PRIMARY KEY NOT NULL,
        #     id_carrinho INT NOT NULL,
        #     id_livro INT NOT NULL,
        #     FOREIGN KEY (id_carrinho) REFERENCES carrinho (id_carrinho),
        #     FOREIGN KEY (id_livro) REFERENCES livro (id_livro)
        # );
        # """
        # self.execute(sql)
        # self.commit()

    #READ/Search
    def read(self, select = '*', id_carrinho = 0, id_item_carrinho = 0, id_livro = 0, search_type = "id_carrinho"):
        try:
            sql = f'SELECT {select} FROM item_carrinho WHERE id_carrinho = {id_carrinho}'

            if search_type == "id_item_carrinho":
                sql = f'SELECT {select} FROM item_carrinho WHERE id_item_carrinho = {id_item_carrinho}'
            elif search_type == "id_livro":
                sql = f'SELECT {select} FROM item_carrinho WHERE id_livro = {id_livro}'

            data = self.query(sql)
            if data:
                return data
            
            return False
        except Exception as error:
            print("Record not found in ItemCarrinhoTable", error)

    def read_all(self, select = '*'):
        try:
            sql = f'SELECT {select} FROM item_carrinho'

            data = self.query(sql)
            if data:
                return data
            
            return False
        except Exception as error:
            print("Record not found in ItemTable", error)

    # INSERT
    def insert(self, id_carrinho = 0, id_livro = 0):
        try:
            sql = f"INSERT INTO item_carrinho (id_carrinho, id_livro) VALUES ({id_carrinho}, {id_livro})"

            self.execute(sql)
            self.commit()
        except Exception as error:
            print("Error inserting record", error)

    # DELETE
    def deleteItem(self, id_item_carrinho = 0, id_livro = 0, delete_type = 'id_livro'):
        try:
            
            sql_search = f"SELECT * FROM item_carrinho WHERE id_livro = {id_livro}"
            if delete_type == 'id_item_carrinho':
                sql_search = f"SELECT * FROM item_carrinho WHERE id_item_carrinho = {id_item_carrinho}"

            if not self.query(sql_search):
                return "Record not found on database"

            sql_delete = f"DELETE FROM item_carrinho WHERE id_livro = {id_livro}"
            if delete_type == 'id_item_carrinho':
                sql_delete = f"DELETE FROM item_carrinho WHERE id_item_carrinho = {id_item_carrinho}"

            self.execute(sql_delete)
            self.commit()
            
        except Exception as error:
            print("Error deleting record", error)

    def deleteAll(self, id_carrinho = 0):
        try:
            sql_search = f"SELECT * FROM item_carrinho WHERE id_carrinho = {id_carrinho}"

            if not self.query(sql_search):
                return "Record not found on database"
            
            
            sql_delete = f"DELETE FROM item_carrinho WHERE id_carrinho = {id_carrinho}"
            
            self.execute(sql_delete)
            self.commit()
            
        except Exception as error:
            print("Error deleting record", error)
