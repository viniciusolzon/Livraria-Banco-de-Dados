import psycopg2
import psycopg2.extras


conn = psycopg2.connect(host = 'localhost', dbname = 'postgres', user = 'postgres', password = '1234', port = 5432)
cur = conn.cursor(cursor_factory= psycopg2.extras.DictCursor)

# faz as coisas
drop_command = "DROP TABLE IF EXISTS person"
cur.execute(drop_command)

cur.execute("""
CREATE SEQUENCE person_id_seq INCREMENT 1;
""")

create__command = """
CREATE TABLE IF NOT EXISTS person(
    id INT PRIMARY KEY NOT NULL DEFAULT nextval('person_id_seq'::regclass),
    name VARCHAR(255),
    age INT,
    gender CHAR,
    weight FLOAT
);
"""
cur.execute(create__command)

insert_command ="""
 INSERT INTO person(id, name, age, gender, weight) VALUES
 (1, 'Mike', 34, 'm', 80.67),
 (2, 'Lisa', 30, 'f', 70.50),
 (3, 'John', 54, 'm', 90.02),
 (4, 'Bob', 80, 'm', 100.13),
 (5, 'Julie', 47, 'f', 60.89);
""" 
cur.execute(insert_command)

# cur.execute("""
# SELECT * FROM person WHERE name = 'Lisa';
# """)
# print(cur.fetchone()) # como o SELECT acima vai dar só um valor a gente usa o fetchone()

# cur.execute("""
# SELECT * FROM person WHERE age <= 54;
# """)
# # print(cur.fetchall()) # como o SELECT acima vai dar mais de um valor a gente usa o fetchall()
# # ou dá pra printar num for tbm
# for row in cur.fetchall():
#     print(row)

cur.execute("SELECT * FROM person;")
for record in cur.fetchall():
    print(record['name'], record['age'])

update_command = "UPDATE person SET age = 45 WHERE name = 'John'"
cur.execute(update_command)
print()

cur.execute("SELECT * FROM person;")
for record in cur.fetchall():
    print(record['name'], record['age'])

delete_command = "DELETE FROM person WHERE name = 'Bob'"
cur.execute(delete_command)
print()
cur.execute("SELECT * FROM person;")
for record in cur.fetchall():
    print(record['name'], record['age'])



conn.commit()

cur.close()
conn.close()
