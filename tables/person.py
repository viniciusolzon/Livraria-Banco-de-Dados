from config import Connection

#Herda de Connection pq vai utilizar os métodos de Connection
class PersonTable(Connection):
    # CREATE
    def __init__(self):
        Connection.__init__(self)
        # Pra não ter que ficar toda hora indo no pgAdmin4 e deletando a tabela manualmente pra executar os comandos sem problema
        self.execute("DROP TABLE IF EXISTS person")
        self.execute("DROP SEQUENCE IF EXISTS person_id_seq")
        self.execute("CREATE SEQUENCE person_id_seq INCREMENT 1;")
        #Cria a tabela se ela ainda não existe
        sql = """
        CREATE TABLE IF NOT EXISTS person(
            id INT PRIMARY KEY NOT NULL DEFAULT nextval('person_id_seq'::regclass),
            name VARCHAR(255),
            age INT,
            gender CHAR
        );
        """
        self.execute(sql)

    #READ/Search
    def read(self, *args, search_type="name"): # A busca padrão é pelo nome
        try:
            sql = "SELECT * FROM person WHERE name LIKE %s"
            # Porém o usuário tbm pode querer pesquisar pelo id
            if search_type == "id":
                sql = "SELECT * FROM person WHERE id = %s"
            data = self.query(sql, args)
            if data:
                return data
            return "Record not found in PersonTable"
                
        except Exception as error:
            print("Record not found in PersonTable", error)

    # UPDATE
    def update(self, id, *args):
        try:
            sql = f"UPDATE person SET name = %s, age = %s, gender = %s WHERE id = {id}"
            self.execute(sql, args)
            self.commit()
            print("Record updated")
        except Exception as error:
            print("Error updating person", error)

    #DELETE
    def delete(self, id):
        try:
            # Busca
            sql_search = f"SELECT * FROM person WHERE id = {id}"
            if not self.query(sql_search):
                return "Record not found on database"
            # Deleta
            sql_delete = f"DELETE FROM person WHERE id = {id}"
            self.execute(sql_delete)
            self.commit()
            return "Record deleted"
        except Exception as error:
            print("Error deleting record", error)
    
    # INSERT
    def insert(self, *args):
        try:
            sql = f"INSERT INTO person (name, age, gender) VALUES (%s, %s, %s)"
            self.execute(sql, args)
            self.commit()
        except Exception as error:
            print("Error inserting record", error)


# Testing
def main():
    person = PersonTable()
    person.insert("Vinicius", 20, "M")
    person.insert("Victor Mororo", 21, "M")
    print(person.query("SELECT * FROM person"))

    # print(person.delete(2)) # deleta o objeto de id = 2
    # print(person.query("SELECT * FROM person"))

    person.update(1, "Freitas", 21, "M")
    print(person.query("SELECT * FROM person"))

    #print(person.read(1, search_type = "id"))# Busca por id
    #print(person.read("Freitas")) # Busca por nome
    print(person.read("%Mororo")) # Busca a partir do nome


if __name__ == "__main__":
    main()
