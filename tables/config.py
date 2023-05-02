import psycopg2 as db

class Config:
    def __init__(self):
        self.config = {
            "postgres": {
                "user": "postgres",
                "password": "1234",
                "host": "localhost",
                "port": "5432",
                "database": "postgres"
            }
        }

class Connection(Config):
    def __init__(self):
        Config.__init__(self)
        try:
            self.conn = db.connect(**self.config["postgres"])
            self.cur = self.conn.cursor()
        except Exception as error:
            print("Error connecting to postgres database", error)
            exit(1)

    # Métodos
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self.conn
    
    @property
    def cursor(self):
        return self.cur
    
    def commit(self):
        return self.connection.commit()
    
    def fetchall(self):
        return self.cursor.fetchall()

    # executa o comando SQL
    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    # executa o comando SQL e dá o fetchall pra pegar os resultados desse comando
    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()
