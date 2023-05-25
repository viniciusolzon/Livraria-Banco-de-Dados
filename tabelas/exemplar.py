from tabelas.config import Connection

# Herda de Connection pq vai utilizar os métodos de Connection
class ExemplarTable(Connection):
    # CREATE
    def __init__(self):
        Connection.__init__(self)
        sql = """
        CREATE TABLE IF NOT EXISTS exemplar(
            id_exemplar SERIAL PRIMARY KEY NOT NULL,
            preco FLOAT NOT NULL,
            id_livro INT NOT NULL,
            FOREIGN KEY (id_livro) REFERENCES livro (id_livro)
        );
        """
            #PRIMARY KEY (id_exemplar),
        self.execute(sql)
        self.commit()
        
        self.columns = ['id_exemplar', 'preco', 'id_livro']

    def getCols(self):
        return self.columns

    # READ/Search
    def read(self, id_livro = 0):
        try:
            sql = f'SELECT quantia FROM exemplar WHERE id_livro = {id_livro}'

            data = self.query(sql)
            if data:
                return data
            
            return False
        except Exception as error:
            print("Record not found in EstoqueTable", error)

    def read_all(self, select = "*"):
        try:
            sql = f'SELECT {select} FROM exemplar'
            
            data = self.query(sql)
            if data:
                return data

            return False
        except Exception as error:
            print("Record not found in EstoqueTable", error)

    # UPDATE
    def update(self, id_livro = 0, quantia = 0):
        try:
            sql = f"UPDATE exemplar SET quantia = {quantia} WHERE id_livro = {id_livro}"

            self.execute(sql)
            self.commit()
            # print("Record updated")
        except Exception as error:
            print("Error updating pedido", error)

    # INSERT
    def insert(self, id_livro, preco):
        try:
            sql = f"INSERT INTO exemplar (id_livro, preco) VALUES ({id_livro}, {preco}); SELECT CURRVAL('exemplar_id_exemplar_seq');"

            self.execute(sql)
            self.commit()
            return self.fetchall()[0][0]
        except Exception as error:
            print("Error inserting record", error)

    # DELETE
    def delete(self, id_exemplar):
        try:
            sql_search = f"SELECT * FROM exemplar WHERE id_exemplar = {id_exemplar}"

            if not self.query(sql_search):
                return "Record not found on database"
            
            sql_delete = f'DELETE FROM exemplar WHERE id_exemplar = {id_exemplar}'
            self.execute(sql_delete)
            self.commit()
            
        except Exception as error:
            print("Error deleting record", error)

    # ADD
    def add(self, id_livro = 0):
        try:
            sql = f"UPDATE exemplar SET quantia = quantia + 1 WHERE id_livro = {id_livro}"

            self.execute(sql)
            self.commit()
            # print("Record updated")
        except Exception as error:
            print("Error adding book to storage", error)

    # REMOVE
    def remove(self, id_livro = 0):
        try:
            sql = f"UPDATE exemplar SET quantia = quantia - 1 WHERE id_livro = {id_livro}"

            self.execute(sql)
            self.commit()
            # print("Record updated")
        except Exception as error:
            print("Error removing book from storage", error)

