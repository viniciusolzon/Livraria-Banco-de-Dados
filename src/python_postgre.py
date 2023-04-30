import psycopg2


conn = psycopg2.connect(host = 'localhost', dbname = 'postgres', user = 'postgres', password = '1234', port = 5432)
cur = conn.cursor()

# faz as coisas
cur.execute("""
CREATE TABLE IF NOT EXISTS person(
    id INT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    gender CHAR,
    weight FLOAT
);
""")

cur.execute("""
INSERT INTO person(id, name, age, gender, weight) VALUES
(1, 'Mike', 34, 'm', 80.67),
(2, 'Lisa', 30, 'f', 70.50),
(3, 'John', 54, 'm', 90.02),
(4, 'Bob', 80, 'm', 100.13),
(5, 'Julie', 40, 'f', 60.89)
""")


conn.commit()

cur.close()
conn.close()
