import psycopg2


conn = psycopg2.connect(host = 'localhost', dbname = 'postgres', user = 'postgres', password = '1234', port = 5432)
cur = conn.cursor()

# faz as coisas
# drop_command = "DROP TABLE IF EXISTS person"
# cur.execute(drop_command)

create__command = """
CREATE TABLE IF NOT EXISTS cliente(
            id_cliente SERIAL PRIMARY KEY,
            name VARCHAR(255),
            username VARCHAR(255),
            password VARCHAR(255),
            email VARCHAR(255)
        );
"""
cur.execute(create__command)

select_command = "SELECT * FROM cliente"
print(cur.execute(select_command))

conn.commit()

cur.close()
conn.close()
