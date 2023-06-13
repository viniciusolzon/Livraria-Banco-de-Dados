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
