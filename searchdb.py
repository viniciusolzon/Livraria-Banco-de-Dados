from tabelas.cliente import ClienteTable
from tabelas.livro import LivroTable
from tabelas.pedido import PedidoTable
from tabelas.exemplar import ExemplarTable
from tabelas.pedido_exemplar import PedidoExemplarTable

import pandas as pd
from tabulate import tabulate

class SearchDB:
    def __init__(self):
        self.tbl_livro = LivroTable()
        self.tbl_cliente = ClienteTable()
        self.tbl_pedido = PedidoTable()
        self.tbl_exemplar = ExemplarTable()
        self.tbl_pedido_exemplar = PedidoExemplarTable()

    def toLivroDF(self, ret):
        if ret == [] or ret == False:
            return None
        return pd.DataFrame(ret, columns=self.tbl_livro.getCols())

    def printLivro(self):
        ret = self.tbl_livro.read_all()
        print("Livro")
        print(tabulate(self.toLivroDF(ret), headers='keys', tablefmt='psql'))
        print('')

    # funciona com parte do titulo do livro tbm (substr)
    def getLivroByNome(self, name):
        name = name.lower()
        sql = f"SELECT * FROM livro WHERE substring(LOWER(unaccent(titulo)),position('{name}' in LOWER(unaccent(titulo))),LENGTH('{name}')) = '{name}';"
        ret = self.tbl_livro.query(sql)
        df = self.toLivroDF(ret)
        return df

    def getLivroByAno(self, ano):
        ret = self.tbl_livro.read(search_type='ano_publicacao', ano_publicacao=ano)
        df = self.toLivroDF(ret)
        return df

    def getLivroByAutor(self, autor):
        sql = f"SELECT * FROM livro WHERE substring(LOWER(unaccent(autor)),position('{autor}' in LOWER(unaccent(autor))),LENGTH('{autor}')) = '{autor}';"
        ret = self.tbl_livro.query(sql)
        df = self.toLivroDF(ret)
        return df

    def getLivroByID(self, id_):
        ret = self.tbl_livro.read(search_type='id', id_livro=id_)
        df = self.toLivroDF(ret)
        return df

    def getLivroQntd(self):
        sql = f"SELECT COUNT(*) FROM livro;"

        ret = self.tbl_livro.query(sql)
        return ret[0][0]




    def toClienteDF(self, ret):
        if ret == [] or ret == False:
            return None
        return pd.DataFrame(ret, columns=self.tbl_cliente.getCols())

    def printCliente(self):
        ret = self.tbl_cliente.read_all()
        print("Cliente")
        print(tabulate(self.toClienteDF(ret), headers='keys', tablefmt='psql'))
        print('')


    def getClienteByNome(self, name):
        name = name.lower()
        sql = f"SELECT * FROM cliente WHERE substring(LOWER(unaccent(nome)),position('{name}' in LOWER(unaccent(nome))),LENGTH('{name}')) = '{name}';"
        ret = self.tbl_cliente.query(sql)
        df = self.toClienteDF(ret)
        return df

    def getClienteByUsuario(self, user):
        user = user.lower()
        ret = self.tbl_cliente.read(search_type='usuario', usuario=user)
        df = self.toClienteDF(ret)
        return df

    def getClienteByEmail(self, email):
        ret = self.tbl_cliente.read(search_type='email', email=email)
        df = self.toClienteDF(ret)
        return df

    def getClienteFlamengo(self):
        ret = self.tbl_cliente.read(search_type='isFlamengo', isFlamengo=True)
        df = self.toClienteDF(ret)
        return df

    def getClienteQntd(self):
        sql = f"SELECT COUNT(*) FROM cliente;"

        ret = self.tbl_cliente.query(sql)
        return ret[0][0]



    def toExemplarDF(self, ret):
        if ret == [] or ret == False:
            return None
        return pd.DataFrame(ret, columns=self.tbl_exemplar.getCols())

    def printExemplar(self):
        ret = self.tbl_exemplar.read_all()
        print("Exemplar")
        print(tabulate(self.toExemplarDF(ret), headers='keys', tablefmt='psql'))
        print('')

    def getQntdExemplarByID(self, id_):
        sql = f"SELECT COUNT(*) FROM exemplar WHERE id_livro = '{id_}';"
        ret = self.tbl_exemplar.query(sql)

        return ret[0][0]


    def getQntdExemplarByNome(self, name):
        name = name.lower()
        sql = f"SELECT COUNT(*) FROM exemplar, livro WHERE exemplar.id_livro = livro.id_livro AND LOWER(unaccent(livro.titulo)) = unaccent('{name}');"
        ret = self.tbl_exemplar.query(sql)

        return ret[0][0]

    def getExemplarQntd(self):
        sql = f"SELECT COUNT(*) FROM exemplar;"

        ret = self.tbl_exemplar.query(sql)
        return ret[0][0]

    def getValorEstocado(self):
        sql = f"SELECT SUM(preco) FROM exemplar;"

        ret = self.tbl_exemplar.query(sql)
        return ret[0][0]



    def toPedidoDF(self, ret):
        if ret == [] or ret == False:
            return None
        return pd.DataFrame(ret, columns=self.tbl_pedido.getCols())

    def printPedido(self):
        ret = self.tbl_pedido.read_all()
        print("Pedido")
        print(tabulate(self.toPedidoDF(ret), headers='keys', tablefmt='psql'))
        print('')

    def getQntdPedidosByUsuario(self, user):
        sql = f"SELECT COUNT(*) FROM pedido WHERE usuario = '{user}';"
        ret = self.tbl_exemplar.query(sql)

        return ret[0][0]

    def getPedidoQntd(self):
        sql = f"SELECT COUNT(*) FROM pedido;"

        ret = self.tbl_pedido.query(sql)
        return ret[0][0]


    def toPedidoExemplarDF(self, ret):
        if ret == [] or ret == False:
            return None
        return pd.DataFrame(ret, columns=self.tbl_pedido_exemplar.getCols())

    def printPedidoExemplar(self):
        ret = self.tbl_pedido_exemplar.read_all()
        print("Pedido_Exemplar")
        print(tabulate(self.toPedidoExemplarDF(ret), headers='keys', tablefmt='psql'))
        print('')



