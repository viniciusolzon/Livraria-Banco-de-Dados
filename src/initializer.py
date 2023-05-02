# aqui iremos preencher as tabelas com os valores que a gente quiser e tal
import sys
sys.path.insert(0, '../tables')

from person import PersonTable

tables = {}

tables['person'] = PersonTable()


tables['person'].insert("Vinicius Freitas", 20)
tables['person'].insert("Victor Mororó", 21)
tables['person'].insert("Marcelo", 21)
tables['person'].insert("Rafael Sobral", 23)
tables['person'].insert("Juliana Dantas", 21)
tables['person'].insert("Anderson Coutinho", 24)
tables['person'].insert("Carlos Vinicius", 23)
tables['person'].insert("Leandro", 21)

