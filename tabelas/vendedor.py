from tabelas.config import Connection

# Herda de Connection pq vai utilizar os métodos de Connection
class VendedorTable(Connection):
    # CREATE
    def __init__(self):
        Connection.__init__(self)
        # sql = """
        # CREATE TABLE IF NOT EXISTS vendedor(
        #     id_vendedor SERIAL PRIMARY KEY NOT NULL,
        #     nome VARCHAR(255) NOT NULL,
        #     usuario VARCHAR(255) NOT NULL,
        #     senha VARCHAR(255) NOT NULL,
        #     email VARCHAR(255) NOT NULL
        # );
        # """
        # self.execute(sql)
        # self.commit()

    # READ/Search
    def read(self, select = '*', id_vendedor = 0, nome = '', usuario = '', email = '', senha = '', search_type = 'nome'):
        try:
            sql = f"SELECT {select} FROM vendedor WHERE nome = '{nome}'"

            if search_type == "id_vendedor":
                sql = f"SELECT {select} FROM vendedor WHERE id_vendedor = {id_vendedor}"
            elif search_type == "usuario":
                sql = f"SELECT {select} FROM vendedor WHERE usuario = '{usuario}'"
            elif search_type ==  "email":
                sql = f"SELECT {select} FROM vendedor WHERE email = '{email}'"
            elif search_type ==  "senha":
                sql = f"SELECT {select} FROM vendedor WHERE senha = '{senha}'"

            data = self.query(sql)
            if data:
                return data
            
            return False
        except Exception as error:
            print("Record not found in VendedorTable", error)

    def read_all(self, select = '*'):
        try:
            sql = f"SELECT {select} FROM vendedor"

            data = self.query(sql)
            if data:
                return data
            
            return False
        except Exception as error:
            print("Record not found in VendedorTable", error)

    # UPDATE
    def update(self, id_vendedor = 0, nome = '', usuario = '', email = '', senha = '', update_type="nome"):
        try:
            sql = f"UPDATE vendedor SET nome = '{nome}' WHERE id_vendedor = {id_vendedor}"
            
            if update_type == "usuario":
                sql = f"UPDATE vendedor SET usuario = '{usuario}' WHERE id_vendedor = {id_vendedor}"
            elif update_type == "email":
                sql = f"UPDATE vendedor SET email = '{email}' WHERE id_vendedor = {id_vendedor}"
            elif update_type == "senha":
                sql = f"UPDATE vendedor SET senha = '{senha}' WHERE id_vendedor = {id_vendedor}"

            self.execute(sql)
            self.commit()
            # print("Record updated")
        except Exception as error:
            print("Error updating vendedor", error)

    # INSERT
    def insert(self, nome = '', usuario = '', email = '', senha = ''):
        try:
            sql = f"INSERT INTO vendedor (nome, usuario, email, senha) VALUES ('{nome}', '{usuario}', '{email}', '{senha}')"

            self.execute(sql)
            self.commit()
        except Exception as error:
            print("Error inserting record", error)

    # DELETE
    def delete(self, id_vendedor = 0):
        try:
            sql_search = f"SELECT * FROM vendedor WHERE id_vendedor = {id_vendedor}"

            if not self.query(sql_search):
                return False
            
            sql_delete = f"DELETE FROM vendedor WHERE id_vendedor = {id_vendedor}"

            self.execute(sql_delete)
            self.commit()
            return False
        except Exception as error:
            print("Error deleting record", error)

# Testando
# tables = {}
# tables['vendedores'] = VendedorTable()
# tables['vendedor'].insert("Vinicius Freitas", "viniciusolzon", "1234", "vinicius@fake.com")

# print(tables['vendedores'].read('nome', email = 'vinicius123.com', search_type='email'))
# print(tables['vendedores'].read('email', usuario = 'viniciusolzon', search_type='usuario'))
# print(tables['vendedores'].read('usuario', nome = 'Vinicius Freitas Schiavinato Olzon', search_type='nome'))

# tables['vendedores'].update(id_vendedor = 1, nome = 'Vinicius Freitas', update_type='nome')
# tables['vendedores'].update(id_vendedor = 1, usuario = 'viniciusolzon', update_type='usuario')
# tables['vendedores'].update(id_vendedor = 1, email = 'vinicius@fake.com', update_type='email')
# tables['vendedores'].update(id_vendedor = 1, senha = '1234', update_type='senha')

# tables['vendedores'].insert("Victor Mororo", "mororo", 'mororo@fake.com', '1234')

# tables['vendedores'].delete(id_vendedor = 1)