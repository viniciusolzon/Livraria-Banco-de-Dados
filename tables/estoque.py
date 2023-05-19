from config import Connection

# Herda de Connection pq vai utilizar os métodos de Connection
class EstoqueTable(Connection):
    # CREATE
    def __init__(self):
        Connection.__init__(self)
        sql = """
        CREATE TABLE IF NOT EXISTS estoque(
            quantia INT,
            id_livro INT,
            FOREIGN KEY (id_livro) REFERENCES livro (id_livro)
        );
        """
        self.execute(sql)
        self.commit()

    # READ/Search
    def read(self, *args):
        try:
            sql = 'SELECT quantia FROM estoque WHERE id_livro = %s'

            data = self.query(sql, args)[0][0]
            if data:
                return data
            
            return "Record not found in EstoqueTable"
                        
        except Exception as error:
            print("Record not found in EstoqueTable", error)

    def read_all(self):
        try:
            sql = 'SELECT * FROM estoque'
            
            data = self.query(sql)[0][0]
            if data:
                return data

            return "Record not found in EstoqueTable"
        
        except Exception as error:
            print("Record not found in EstoqueTable", error)

    # INSERT
    def insert(self, *args):
        try:
            
            sql_search = "SELECT * FROM livro WHERE id_livro = '%s'"

            if not self.query(sql_search):
                return "Record not found on database"
            
            sql_update = 'UPDATE estoque SET quantia = quantia + 1 WHERE id_livro = "%s"'
            self.execute(sql_update, args)
            self.commit()
            
        except Exception as error:
            print("Error inserting record", error)


    # DELETE
    def delete(self, *args):
        try:
            
            sql_search = "SELECT * FROM livro WHERE id_livro = '%s'"

            if not self.query(sql_search):
                return "Record not found on database"
            
            sql_delete = 'UPDATE estoque SET quantia = quantia - 1 WHERE id_livro = "%s"'
            self.execute(sql_delete, args)
            self.commit()
            
        except Exception as error:
            print("Error deleting record", error)
