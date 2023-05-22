from tabelas.cliente import ClienteTable
from tabelas.livro import LivroTable
from tabelas.pedido import PedidoTable
from tabelas.estoque import EstoqueTable

tables = {}

tables['livro'] = LivroTable()
tables['cliente'] = ClienteTable()
tables['pedido'] = PedidoTable()
tables['estoque'] = EstoqueTable()

# Preenchendo a tabela de livros
# tables['livro'].insert("Codigo Limpo", "Robert Cecil Martin", 2008, 69.99)
# tables['livro'].insert("Romeu e Julieta", "William Shakespeare", 1595, 59.99)
# tables['livro'].insert("Contos De Voltaire", "Voltaire", 1972, 84.99)
# tables['livro'].insert("Senhor das moscas", "William Golding", 1954, 79.99)
# tables['livro'].insert("O Pequeno Principe", "Antoine de Saint-Exupéry", 1943, 31.99)
# tables['livro'].insert("O Cortiço", "Aluísio Azevedo", 1890, 27.99)


# Preenchendo a tabela de cliente
# tables['cliente'].insert("Vinicius Freitas", "viniciusolzon", "vinicius@fake.com", "1234")
# tables['cliente'].insert("Victor Mororo", "mororo", "victor@fake.com", "4321")

# Preenchendo a tabela de vendas
