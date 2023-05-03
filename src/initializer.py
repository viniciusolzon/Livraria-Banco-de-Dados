# aqui iremos preencher as tabelas com os valores que a gente quiser e tal
import sys
sys.path.insert(0, '../tables')

from usuario import UsuarioTable
from livro import LivroTable

tables = {}

tables['usuario'] = UsuarioTable()
tables['livro'] = LivroTable()

# Preenchendo a tablea de usuarios
tables['usuario'].insert("Vinicius Freitas", "vinicius@123.fake.com")
tables['usuario'].insert("Victor Mororó", "victor@123.fake.com")
tables['usuario'].insert("Rafael Sobral", "rafael@123.fake.com")
tables['usuario'].insert("Juliana Dantas", "juliana@123.fake.com")
tables['usuario'].insert("Anderson Coutinho", "anderson@123.fake.com")
tables['usuario'].insert("Carlos Vinicius", "carlos@123.fake.com")
tables['usuario'].insert("Leandro", "leandro@123.fake.com")


# Preenchendo a tablea de livros
tables['livro'].insert("Codigo Limpo", "Estudo Cientifico", "Robert Cecil Martin", 2008)
tables['livro'].insert("Romeu e Julieta", "Tragédia", "William Shakespeare", 1595)
tables['livro'].insert("Contos De Voltaire", "Contos", "Voltaire", 1972)
tables['livro'].insert("Senhor das moscas", "Romance", "William Golding", 1954)
tables['livro'].insert("O Pequeno Principe", "Folclore", "Antoine de Saint-Exupéry", 1943)
