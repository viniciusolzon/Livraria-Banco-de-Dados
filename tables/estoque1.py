from config import Connection
from fmt_sql import fmtSQL

# Herda de Connection pq vai utilizar os métodos de Connection
class EstoqueTable(Connection):
    # CREATE
    def __init__(self):
        Connection.__init__(self)
        # Pra não ter que ficar toda hora indo no pgAdmin4 e deletando a tabela manualmente pra executar os comandos sem problema
        # self.execute("DROP TABLE IF EXISTS estoque")
        # Cria a tabela se ela ainda não existe
        sql = """
        CREATE TABLE IF NOT EXISTS estoque(
            quantia INT,
            titulo_livro,
            FOREIGN KEY (titulo_livro) REFERENCES livro (titulo)
        );
        """
        self.execute(sql)
        self.commit()

    # READ/Search
    def read(self, *args, select = '*', search_type = 'titulo'): # A busca padrão é pelo id
        try:
            sql = fmtSQL() \
                    .SELECT(select) \
                    .FROM('estoque')

            if search_type == 'titulo':
                sql.WHERE('titulo = %s')
            data = self.query(sql, args)
            
            if data:
                return data
            
            return "Record not found in EstoqueTable"
                
        except Exception as error:
            print("Record not found in EstoqueTable", error)

    def read_all(self):
        try:
            sql = fmtSQL() \
                    .SELECT() \
                    .FROM('estoque')
            data = self.query(sql)

            if data:
                return data

            return "Record not found in EstoqueTable"
        
        except Exception as error:
            print("Record not found in EstoqueTable", error)

    # UPDATE
    def update(self, id, *args, update_type="quantia"):
        try:
            sql = fmtSQL() \
                    .UPDATE('estoque')

            if update_type == "quantia":
                sql.SET('quantia = %s')

            sql.WHERE(f'id_pedido = {id}')
            self.execute(sql, args)
            self.commit()
            print("Record updated")
            
        except Exception as error:
            print("Error updating estoque", error)

    # DELETE
    def delete(self, titulo):
        try:
            sql = fmtSQL() \
                    .FROM('estoque') \
                    .WHERE(f'titulo = {titulo}')
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
                    .INSERT_INTO('estoque', '(quantia, titulo_livro)') \
                    .VALUES('(%s, %s)')
            self.execute(sql, args)
            self.commit()
            
        except Exception as error:
            print("Error inserting record", error)
