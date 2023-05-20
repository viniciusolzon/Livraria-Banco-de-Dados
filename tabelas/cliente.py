from tabelas.config import Connection

# Herda de Connection pq vai utilizar os métodos de Connection
class ClienteTable(Connection):
    # CREATE
    def __init__(self):
        Connection.__init__(self)
        sql = """
        CREATE TABLE IF NOT EXISTS cliente(
            id_cliente SERIAL PRIMARY KEY NOT NULL,
            nome VARCHAR(255) NOT NULL,
            usuario VARCHAR(255) NOT NULL,
            senha VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL
        );
        """
        self.execute(sql)
        self.commit()

    # READ/Search
    def read(self, select,  id_cliente = 0, nome = '', usuario = '', email = '', search_type = 'nome'):
        try:
            sql = f"SELECT {select} FROM cliente WHERE nome = '{nome}'"

            if search_type == "id_cliente":
                sql = f"SELECT {select} FROM cliente WHERE id_cliente = {id_cliente}"
            elif search_type == "usuario":
                sql = f"SELECT {select} FROM cliente WHERE usuario = '{usuario}'"
            elif search_type ==  "email":
                sql = f"SELECT {select} FROM cliente WHERE email = '{email}'"

            data = self.query(sql)[0][0]
            if data:
                return data
            
            return False
        except Exception as error:
            print("Record not found in ClienteTable", error)

    def read_all(self, id_cliente = 0):
        try:
            sql = f"SELECT * FROM cliente WHERE id_cliente = {id_cliente}"

            data = self.query(sql)[0][0]
            if data:
                return data
            
            return False
        except Exception as error:
            print("Record not found in ClienteTable", error)

    # UPDATE
    def update(self, id_cliente, nome = '', usuario = '', email = '', senha = '', update_type="nome"):
        try:
            sql = f"UPDATE cliente SET nome = '{nome}' WHERE id_cliente = {id_cliente}"
            
            if update_type == "usuario":
                sql = f"UPDATE cliente SET usuario = '{usuario}' WHERE id_cliente = {id_cliente}"
            elif update_type == "email":
                sql = f"UPDATE cliente SET email = '{email}' WHERE id_cliente = {id_cliente}"
            elif update_type == "senha":
                sql = f"UPDATE cliente SET senha = '{senha}' WHERE id_cliente = {id_cliente}"

            self.execute(sql)
            self.commit()
            # print("Record updated")
        except Exception as error:
            print("Error updating cliente", error)

    # INSERT
    def insert(self, nome, usuario, email, senha):
        try:
            sql = f"INSERT INTO cliente (nome, usuario, email, senha) VALUES ('{nome}', '{usuario}', '{email}', '{senha}')"

            self.execute(sql)
            self.commit()
        except Exception as error:
            print("Error inserting record", error)

    # DELETE
    def delete(self, id_cliente):
        try:
            sql_search = f"SELECT * FROM cliente WHERE id_cliente = {id_cliente}"

            if not self.query(sql_search):
                return False
            
            sql_delete = f"DELETE FROM cliente WHERE id_cliente = {id_cliente}"

            self.execute(sql_delete)
            self.commit()
            return False
        except Exception as error:
            print("Error deleting record", error)

# Testando
# tables = {}
# tables['clientes'] = ClienteTable()
# tables['cliente'].insert("Vinicius Freitas", "viniciusolzon", "1234", "vinicius@fake.com")

# print(tables['clientes'].read('nome', email = 'vinicius123.com', search_type='email'))
# print(tables['clientes'].read('email', usuario = 'viniciusolzon', search_type='usuario'))
# print(tables['clientes'].read('usuario', nome = 'Vinicius Freitas Schiavinato Olzon', search_type='nome'))

# tables['clientes'].update(id_cliente = 1, nome = 'Vinicius Freitas', update_type='nome')
# tables['clientes'].update(id_cliente = 1, usuario = 'viniciusolzon', update_type='usuario')
# tables['clientes'].update(id_cliente = 1, email = 'vinicius@fake.com', update_type='email')
# tables['clientes'].update(id_cliente = 1, senha = '1234', update_type='senha')

# tables['clientes'].insert("Victor Mororo", "mororo", 'mororo@fake.com', '1234')

# tables['clientes'].delete(id_cliente = 5)
