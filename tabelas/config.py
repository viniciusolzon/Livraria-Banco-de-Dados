import psycopg2 as db

class Connection():
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
        try:
            self.conn = db.connect(**self.config["postgres"])
            self.cur = self.conn.cursor()
            self.cur.execute("CREATE EXTENSION IF NOT EXISTS unaccent;")
        except Exception as error:
            print("Error connecting to postgres database", error)
            exit(1)

    def __enter__(self):
        return self
    
    def __exit__(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def commit(self):
        return self.conn.commit()
    
    def fetchall(self):
        try:
            return self.cur.fetchall()
        except Exception as error:
            print(error)
            self.conn.rollback()

    # executa o comando SQL
    def execute(self, sql, params=None):
        print(sql)
        try:
            self.cur.execute(sql, params or ())
        except Exception as error:
            print(error)
            self.conn.rollback()

    # executa o comando SQL e dá o fetchall pra pegar os resultados desse comando
    def query(self, sql, params=None):
        print(sql)
        ret = None
        try:
            self.cur.execute(str(sql), params or ())
            ret = self.fetchall()
        except Exception as error:
            print(error)
            self.conn.rollback()

        return ret
