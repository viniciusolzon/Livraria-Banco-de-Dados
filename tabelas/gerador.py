from tabelas.cliente import ClienteTable
from tabelas.livro import LivroTable
from tabelas.pedido import PedidoTable

tables = {}

tables['livro'] = LivroTable()
tables['cliente'] = ClienteTable()
tables['pedido'] = PedidoTable()

# Preenchendo a tabela de livros (rode o código uma vez com isso debaixo descomentado para preencher as tableas)
# tables['livro'].insert(titulo = "Codigo Limpo", autor = "Robert Cecil Martin", ano_publicacao = 2008, preco = 69.99)
# tables['livro'].insert(titulo = "Romeu e Julieta", autor = "William Shakespeare", ano_publicacao = 1595,preco =  59.99)
# tables['livro'].insert(titulo = "Contos De Voltaire", autor = "Voltaire", ano_publicacao = 1972,preco =  84.99)
# tables['livro'].insert(titulo = "Senhor das moscas", autor = "William Golding", ano_publicacao = 1954, preco = 79.99)
# tables['livro'].insert(titulo = "O Pequeno Principe", autor = "Antoine de Saint-Exupéry", ano_publicacao = 1943, preco = 31.99)
# tables['livro'].insert(titulo = "O Cortiço", autor = "Aluísio Azevedo", ano_publicacao = 1890, preco = 27.99)


# Preenchendo a tabela de cliente (rode o código uma vez com isso debaixo descomentado para preencher as tableas)
# tables['cliente'].insert(nome = "Vinicius Freitas", usuario = "viniciusolzon", email = "vinicius@fake.com", senha = "1234", isFlamengo = False)
# tables['cliente'].insert(nome = "Victor Mororo", usuario = "mororo", email = "victor@fake.com", senha = "4321",  isFlamengo = True)
