# aqui iremos preencher as tabelas com os valores que a gente quiser e tal
import sys
sys.path.insert(0, '../tables')

from usuario import UsuarioTable
from livro import LivroTable
# from pedido import PedidoTable
# from carrinho import CarrinhoTable

tables = {}

tables['usuario'] = UsuarioTable()
tables['livro'] = LivroTable()
# tables['pedido'] = PedidoTable()
# tables['carrinho'] = Carrinhotable()


# Preenchendo a tabela de usuarios
tables['usuario'].insert("Vinicius Freitas", "vinicius@123.fake.com")
tables['usuario'].insert("Victor Mororo", "victor@123.fake.com")
tables['usuario'].insert("Rafael Sobral", "rafael@123.fake.com")
tables['usuario'].insert("Juliana Dantas", "juliana@123.fake.com")
tables['usuario'].insert("Anderson Coutinho", "anderson@123.fake.com")
tables['usuario'].insert("Carlos Vinicius", "carlos@123.fake.com")
tables['usuario'].insert("Leandro", "leandro@123.fake.com")


# Preenchendo a tabela de livros
tables['livro'].insert(69.99, "Codigo Limpo", "Estudo Cientifico", "Robert Cecil Martin", 2008)
tables['livro'].insert(59.99, "Romeu e Julieta", "Tragédia", "William Shakespeare", 1595)
tables['livro'].insert(84.99, "Contos De Voltaire", "Contos", "Voltaire", 1972)
tables['livro'].insert(79.99, "Senhor das moscas", "Romance", "William Golding", 1954)
tables['livro'].insert(31.99, "O Pequeno Principe", "Folclore", "Antoine de Saint-Exupéry", 1943)


# Preenchendo a tabela de usuarios



# Preenchendo a tabela de usuarios
