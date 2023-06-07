from tabelas.config import Connection

# Herda de Connection pq vai utilizar os métodos de Connection
class EstoqueTable(Connection):
    # CREATE
    def __init__(self):
        Connection.__init__(self)
        sql = """
        CREATE TABLE IF NOT EXISTS estoque(
            titulo_livro INT NOT NULL,
            quantia INT NOT NULL,
            FOREIGN KEY (titulo_livro) REFERENCES livro (titulo_livro)
        );
        """
        self.execute(sql)
        self.commit()

    # READ/Search
    def read(self, titulo_livro = 0):
        try:
            sql = f'SELECT quantia FROM estoque WHERE titulo_livro = {titulo_livro}'

            data = self.query(sql)
            if data:
                return data
            
            return False
        except Exception as error:
            print("Record not found in EstoqueTable", error)

    def read_all(self, select = "*"):
        try:
            sql = f'SELECT {select} FROM estoque'
            
            data = self.query(sql)
            if data:
                return data

            return False
        except Exception as error:
            print("Record not found in EstoqueTable", error)

    # UPDATE
    def update(self, titulo_livro = 0, quantia = 0):
        try:
            sql = f"UPDATE estoque SET quantia = {quantia} WHERE titulo_livro = {titulo_livro}"

            self.execute(sql)
            self.commit()
            # print("Record updated")
        except Exception as error:
            print("Error updating estoque", error)

    # INSERT
    def insert(self, titulo_livro = 0, quantia = 0):
        try:
            sql = f"INSERT INTO estoque (titulo_livro, quantia) VALUES ({titulo_livro}, {quantia})"

            self.execute(sql)
            self.commit()
        except Exception as error:
            print("Error inserting record", error)

    # DELETE
    def delete(self, titulo_livro = 0):
        try:
            sql_search = f"SELECT * FROM estoque WHERE titulo_livro = {titulo_livro}"

            if not self.query(sql_search):
                return "Record not found on database"
            
            sql_delete = f'DELETE FROM estoque WHERE titulo_livro = {titulo_livro}'
            self.execute(sql_delete)
            self.commit()
            
        except Exception as error:
            print("Error deleting record", error)

    # ADD
    def add(self, titulo_livro = 0):
        try:
            sql = f"UPDATE estoque SET quantia = quantia + 1 WHERE titulo_livro = {titulo_livro}"

            self.execute(sql)
            self.commit()
            # print("Record updated")
        except Exception as error:
            print("Error adding book to storage", error)

    # REMOVE
    def remove(self, titulo_livro = 0):
        try:
            sql = f"UPDATE estoque SET quantia = quantia - 1 WHERE titulo_livro = {titulo_livro}"

            self.execute(sql)
            self.commit()
            # print("Record updated")
        except Exception as error:
            print("Error removing book from storage", error)

