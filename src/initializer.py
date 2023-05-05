# aqui iremos preencher as tabelas com os valores que a gente quiser e tal
import sys
sys.path.insert(0, '../tables')

from cliente import ClienteTable
from livro import LivroTable
# from venda import VendaTable
# from biblioteca import BibliotecaTable

tables = {}

tables['cliente'] = ClienteTable()
tables['livro'] = LivroTable()
# tables['venda'] = VendaTable()


# Preenchendo a tabela de cliente
# tables['cliente'].insert("Vinicius Freitas", "viniciusolzon", "1234", "vinicius@fake.com")
# tables['cliente'].insert("Victor Mororo", "mororo", "4321", "victor@fake.com")
# tables['cliente'].insert("Rafael Sobral", "rafael@fake.com")
# tables['cliente'].insert("Juliana Dantas", "juliana@fake.com")
# tables['cliente'].insert("Anderson Coutinho", "anderson@fake.com")
# tables['cliente'].insert("Carlos Vinicius", "carlos@fake.com")
# tables['cliente'].insert("Leandro", "leandro@fake.com")


# Preenchendo a tabela de livros
tables['livro'].insert(69.99, "Código Limpo", "Estudo Cientifico", "Robert Cecil Martin", 2008)
tables['livro'].insert(59.99, "Romeu e Julieta", "Tragédia", "William Shakespeare", 1595)
tables['livro'].insert(84.99, "Contos De Voltaire", "Contos", "Voltaire", 1972)
tables['livro'].insert(79.99, "Senhor das moscas", "Romance", "William Golding", 1954)
tables['livro'].insert(31.99, "O Pequeno Príncipe", "Folclore", "Antoine de Saint-Exupéry", 1943)
tables['livro'].insert(27.99, "O Cortiço", "Romance", "Aluísio Azevedo", 1890)


# Preenchendo a tabela de pedidos


