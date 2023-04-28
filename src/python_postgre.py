import psycopg2


conn = psycopg2.connect(host = 'localhost', dbname = 'demo', user = 'postgres', password = '12345', port = 5432)
cur = conn.cursor()

# faz as coisas 


conn.commit()

cur.close()
conn.close()
