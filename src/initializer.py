# aqui iremos preencher as tabelas com os valores que a gente quiser e tal
import sys
sys.path.insert(0, '../tables')

from usuario import PersonTable

tables = {}

tables['usuario'] = PersonTable()


tables['usuario'].insert("Vinicius Freitas", 20)
tables['usuario'].insert("Victor Mororó", 21)
tables['usuario'].insert("Marcelo", 21)
tables['usuario'].insert("Rafael Sobral", 23)
tables['usuario'].insert("Juliana Dantas", 21)
tables['usuario'].insert("Anderson Coutinho", 24)
tables['usuario'].insert("Carlos Vinicius", 23)
tables['usuario'].insert("Leandro", 21)

