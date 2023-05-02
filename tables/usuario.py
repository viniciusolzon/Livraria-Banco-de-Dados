from config import Connection

#Herda de Connection pq vai utilizar os métodos de Connection
class PersonTable(Connection):
    # CREATE
    def __init__(self):
        Connection.__init__(self)
        # Pra não ter que ficar toda hora indo no pgAdmin4 e deletando a tabela manualmente pra executar os comandos sem problema
        self.execute("DROP TABLE IF EXISTS usuario")
        #self.execute("DROP SEQUENCE IF EXISTS person_id_seq")
        #self.execute("CREATE SEQUENCE person_id_seq INCREMENT 1;")
        #Cria a tabela se ela ainda não existe
        sql = """
        CREATE TABLE IF NOT EXISTS usuario(
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            age INT
        );
        """
        # Antes o id tava assim: id INT PRIMARY KEY NOT NULL DEFAULT nextval('person_id_seq'::regclass),
        
        
        self.execute(sql)

    #READ/Search
    def read(self, *args, search_type="name"): # A busca padrão é pelo nome
        try:
            sql = "SELECT * FROM usuario WHERE name LIKE %s"
            # Porém o usuário tbm pode querer pesquisar pelo id
            if search_type == "id":
                sql = "SELECT * FROM usuario WHERE id = %s"
            data = self.query(sql, args)
            if data:
                return data
            return "Record not found in PersonTable"
                
        except Exception as error:
            print("Record not found in PersonTable", error)

    # UPDATE
    def update(self, id, *args):
        try:
            sql = f"UPDATE usuario SET name = %s, age = %s, gender = %s WHERE id = {id}"
            self.execute(sql, args)
            self.commit()
            print("Record updated")
        except Exception as error:
            print("Error updating usuario", error)

    #DELETE
    def delete(self, id):
        try:
            # Busca
            sql_search = f"SELECT * FROM usuario WHERE id = {id}"
            if not self.query(sql_search):
                return "Record not found on database"
            # Deleta
            sql_delete = f"DELETE FROM usuario WHERE id = {id}"
            self.execute(sql_delete)
            self.commit()
            return "Record deleted"
        except Exception as error:
            print("Error deleting record", error)
    
    # INSERT
    def insert(self, *args):
        try:
            sql = f"INSERT INTO usuario (name, age) VALUES (%s, %s)"
            self.execute(sql, args)
            self.commit()
        except Exception as error:
            print("Error inserting record", error)


# Testing
# def main():
#     usuario = PersonTable()
#     usuario.insert("Vinicius", 20)
#     usuario.insert("Victor Mororo", 21)
#     usuario.insert("Gabriel Freitas", 24)
    
#     # for row in usuario.query("SELECT * FROM usuario"):
#     #     print(row)
        
#     #print(usuario.query("SELECT * FROM usuario"))

#     # print(usuario.delete(2)) # deleta o objeto de id = 2
#     # print(usuario.query("SELECT * FROM usuario"))

#     #usuario.update(1, "Freitas", 21)
#     #print(usuario.query("SELECT * FROM usuario"))

#     #print(usuario.read(1, search_type = "id"))# Busca por id
#     #print(usuario.read("Freitas")) # Busca por nome
#     #print(usuario.read("%Mororo")) # Busca a partir do nome


# if __name__ == "__main__":
#     main()
