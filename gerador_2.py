from tabelas.cliente import ClienteTable
from tabelas.livro import LivroTable
from tabelas.pedido import PedidoTable
from tabelas.exemplar import ExemplarTable
from tabelas.pedido_exemplar import PedidoExemplarTable

tables = {}

tables['livro'] = LivroTable()
tables['cliente'] = ClienteTable()
tables['pedido'] = PedidoTable()
tables['exemplar'] = ExemplarTable()
tables['pedido_exemplar'] =  PedidoExemplarTable()

# Preenchendo a tabela de livros (rode o código uma vez com isso debaixo descomentado para preencher as tableas)
#tables['livro'].insert(id_livro = 4, titulo = "Codigo Limpo", autor = "Robert Cecil Martin", ano_publicacao = 2008)
#tables['livro'].insert(id_livro = 5, titulo = "Romeu e Julieta", autor = "William Shakespeare", ano_publicacao = 1595)
#tables['livro'].insert(id_livro = 6, titulo = "Contos De Voltaire", autor = "Voltaire", ano_publicacao = 1972)
#tables['livro'].insert(id_livro = 7, titulo = "Senhor das moscas", autor = "William Golding", ano_publicacao = 1954)
tables['livro'].insert(id_livro = 8, titulo = "O Pequeno Principe", autor = "Antoine de Saint-Exupéry", ano_publicacao = 1943)
tables['livro'].insert(id_livro = 9, titulo = "O Cortiço", autor = "Aluísio Azevedo", ano_publicacao = 1890)

#tables['exemplar'].insert(id_livro=4, preco=43)
#tables['exemplar'].insert(id_livro=4, preco=43)
id_ex1 = tables['exemplar'].insert(id_livro=4, preco=43)
id_ex2 = tables['exemplar'].insert(id_livro=9, preco=33)
print(id_ex1, id_ex2)
#tables['exemplar'].insert(id_livro=9, preco=13)


# Preenchendo a tabela de cliente (rode o código uma vez com isso debaixo descomentado para preencher as tableas)
tables['cliente'].insert(nome = "Vinicius Freitas", usuario = "viniciusolzon", email = "vinicius@fake.com", senha = "1234", isFlamengo = False)
tables['cliente'].insert(nome = "Victor Mororo", usuario = "mororo", email = "victor@fake.com", senha = "4321",  isFlamengo = True)

#tables['pedido'].insert(usuario = 'mororo', custo=30)
#tables['pedido'].insert(usuario = 'mororo', custo=25)
id_pedido = tables['pedido'].insert(usuario = 'viniciusolzon', custo=76)


tables['pedido_exemplar'].insert(id_exemplar = id_ex1, id_pedido=id_pedido)
tables['pedido_exemplar'].insert(id_exemplar = id_ex2, id_pedido=id_pedido)



### REMOCAO ###

tables['livro'].delete(id_livro=8)
tables['exemplar'].delete(id_exemplar=id_ex1)
tables['cliente'].delete(usuario='mororo')
tables['pedido'].delete(id_pedido=id_pedido)
tables['pedido_exemplar'].delete(id_pedido=id_pedido, id_exemplar=id_ex2)

### LISTAR ###

from searchdb import SearchDB

srch = SearchDB()

srch.printLivro()
srch.printCliente()
srch.printExemplar()
srch.printPedido()
srch.printPedidoExemplar()


### Pesquisa ###
srch.getLivroByNome('limpo')
srch.getLivroByAno(1595)
srch.getLivroByAutor('exupery')
srch.getLivroByID(8)


srch.getClienteByNome('vinicius')
srch.getClienteByUsuario('viniciusolzon')
srch.getClienteByEmail('vinicius@fake.com')
srch.getClienteFlamengo()

srch.getQntdExemplarByNome('codigo limpo')
srch.getQntdExemplarByID(4)

srch.getQntdPedidosByUsuario('mororo')

q = srch.getLivroQntd()
q = srch.getClienteQntd()
q = srch.getPedidoQntd()
q = srch.getExemplarQntd()

q = srch.getValorEstocado()
print(q)
