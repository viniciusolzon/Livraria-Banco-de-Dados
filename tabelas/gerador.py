from tabelas.livro import LivroTable
from tabelas.cliente import ClienteTable
from tabelas.vendedor import VendedorTable
from tabelas.carrinho import CarrinhoTable
from tabelas.pedido import PedidoTable
from tabelas.item_carrinho import ItemCarrinhoTable
from tabelas.item_pedido import ItemPedidoTable
from tabelas.estoque import EstoqueTable

tables = {}

tables['livro'] = LivroTable()
tables['cliente'] = ClienteTable()
tables['vendedor'] = VendedorTable()
tables['carrinho'] = CarrinhoTable()
tables['pedido'] = PedidoTable()
tables['item_carrinho'] = ItemCarrinhoTable()
tables['item_pedido'] = ItemPedidoTable()
tables['estoque'] = EstoqueTable()

# Preenchendo a tabela de livros (rode o código uma vez com isso debaixo descomentado para preencher as tabelas)
# Dá pra inserir sem acento e tudo minusculo, na busca a gente procura sem acento e tudo minusculo entao nao tem problema
# tables['livro'].insert(titulo = "Codigo Limpo", autor = "Robert Cecil Martin", ano_publicacao = 2008, preco = 49.99)
# tables['livro'].insert(titulo = "Romeu e Julieta", autor = "William Shakespeare", ano_publicacao = 1595,preco =  9.99)
# tables['livro'].insert(titulo = "Contos de Voltaire", autor = "Voltaire", ano_publicacao = 1972,preco =  84.99)
# tables['livro'].insert(titulo = "Senhor das Moscas", autor = "William Golding", ano_publicacao = 1954, preco = 39.99)
# tables['livro'].insert(titulo = "O Pequeno Principe", autor = "Antoine de Saint Exupéry", ano_publicacao = 1943, preco = 31.99)
# tables['livro'].insert(titulo = "O Cortiço", autor = "Aluísio Azevedo", ano_publicacao = 1890, preco = 27.99)
# tables['livro'].insert(titulo = "100 Anos de Solidao", autor = "Gabriel Garcia Marquez", ano_publicacao = 1982, preco = 34.99)
# tables['livro'].insert(titulo = "A Hora da Estrela", autor = "Clarice Lispector", ano_publicacao = 1977, preco = 19.99)
# tables['livro'].insert(titulo = "Memorias Postumas de Bras Cubas", autor = "Machado de Assis", ano_publicacao = 1881, preco = 14.99)

# insere 10 exemplares de cada titulo
# id_livros = tables['livro'].read_all('id_livro')
# if id_livros:
    # for id in id_livros:
        # tables['estoque'].insert(id_livro = id[0], quantia = 10)

# Precisa sempre ter um vendedor cadastrado
# tables['vendedor'].insert(nome = "Vinicius Freitas", usuario = "vinicius", email = "vinicius@fake.com", senha = "123")
