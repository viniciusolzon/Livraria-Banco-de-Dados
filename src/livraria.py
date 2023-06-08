from src.help import *


class Livraria():
    def __init__(self, nome = "Tuko"):
        self.nome = nome
        self.logado = False
        self.usuario_logado = "Desconhecido"
    
    def Initialize(self):
        print(f"\n\tOlá seja bem vindo a livraria {self.nome}!\n")
        if self.logado:
            self.menuUsuario()
        else:
            self.menuPrincipal()
    
    def menuPrincipal(self):
        menu_c = ["L", "C", "P", "U", "V", "Q"]
        print("O que deseja fazer?")
        while True:
            choice = input( 
                    "* (L) Realizar login \n"
                    "* (C) Realizar cadastro \n"
                    "* (P) Pesquisar livro \n"
                    "* (U) Ver clientes cadastrados \n"
                    "* (V) Ver vendas da livraria \n"
                    "* (Q) Sair do sistema \n"
                    "-> "
                    )
            
            choice = choice.upper()

            if choice not in  menu_c:
                print("\nDesculpe, tente novamente...\n")
                continue
            else:
                break

        if choice   == "L":
            self.Login()
        elif choice == "C":
            self.Register()
        elif choice == "P":
            clear_terminal()
            self.bookSearch()
        elif choice == "U":
            self.mostra_clientes()
        elif choice == "V":
            self.mostra_vendas()
        elif choice == "Q":
            quitLibrary()
        else:
            print("Deu ruim")
            exit(-666)

    def menuUsuario(self):
        print(f"\n\tOlá seja bem vindo de volta {self.usuario_logado}!\n")
        menu_c = ["C", "P", "E", "D", "S", "Q"]
        print("O que deseja fazer?")
        while True:
            choice = input(
                    "* (C) Realizar pedido\n"
                    "* (P) Ver todos seus pedidos\n"
                    "* (E) Carrinho de compras\n"
                    "* (D) Ver seus dados cadastrais\n"
                    "* (S) Sair da conta\n"
                    "* (Q) Sair do sistema\n"
                    "-> "
                    )

            choice = choice.upper()

            if choice not in  menu_c:
                print("\nDesculpe, tente novamente...\n")
                continue
            else:
                break

        if choice   == "C":
            clear_terminal()
            self.bookSearch()
        elif choice == "P":
            self.verPedidos()
        elif choice == "E":
            clear_terminal()
            self.menuCarrinho()
        elif choice == "D":
            self.verDadosCadastrais()
        elif choice == "S":
            clear_terminal()
            self.logado = False
            self.usuario_logado = "Desconhecido"
            print("\nCliente deslogado.")
            print("Voltando ao menu principal...\n")
            self.menuPrincipal()
        elif choice == "Q":
            quitLibrary()
        else:
            print("Deu ruim")
            exit(-666)
    
    def registered(self, Nome, Usuario, Email, Senha, flamengo):
        tables['cliente'].insert(nome = Nome, usuario = Usuario, email = Email, senha = Senha, isFlamengo = flamengo)
        
        idCliente = tables['cliente'].read('id_cliente', usuario = Usuario, search_type = 'usuario')[0][0]
        tables['carrinho'].insert(id_cliente = idCliente)
        
        clear_terminal()
        print("\n\tRegistro feito com sucesso!\n")
        self.menuPrincipal()
        quit()

    def Login(self):
        clear_terminal()
        print("\n\tTela de Login\n")
            
        usuario = input("\n\tNome de usuário: ")
        if (checkUsername(usuario)):
            # print("\n\tEsse nome de usuário ainda não possui cadastro na livraria, voltando ao menu principal...\n")
            print("\n\tEsse nome de usuário ainda não possui cadastro na livraria, deseja fazer o cadastro?\n")
            deseja = SimNao()

            if deseja == "S" or deseja == "SIM":
                self.Register()
            else:
                clear_terminal()
                print("\nVoltando ao menu principal...\n")
                self.menuPrincipal()
                quit()

        senha = input("\tSenha: ")
        if (not checkPassword(usuario, senha)):
            print("\n\tA senha inserida não coincide com o usuário cadastrado, tente novamente:\n")
            senha = input("\tSenha: ")
            if (not checkPassword(usuario, senha)):
                print("\n\tA senha inserida não coincide com o usuário cadastrado, voltando ao menu principal...\n")
                self.menuPrincipal()
                quit()

        clear_terminal()
        self.logado = True
        self.usuario_logado = usuario
        self.menuUsuario()
        quit()


    def Register(self):
        clear_terminal()
        print("\n\tTela de Cadastro\n")
            
        # aqui não precisa de verificação nenhuma pq podem existir vários usuários com o mesmo nome
        name = input("\nNome completo: ")

        email = input("Email: ")
        if(not checkEmail(email)):
            print("\n\tO email inserido já possui cadastro na livraria, voltando ao menu principal...\n")
            self.menuPrincipal()
            quit()

        usuario = input("Nome de usuário: ")
        if(not checkUsername(usuario)):
            print("\n\tEsse nome de usuário já possui cadastro na livraria, voltando ao menu principal...\n")
            self.menuPrincipal()
            quit()

        senha = input("Senha: ")
        senha_verificacao = input("Verificação da senha: ")
        
        if senha != senha_verificacao:
            print("\nAs senhas digitadas não coincidem, por favor tente novamente:")
            senha = input("Senha: ")
            senha_verificacao = input("Verificação da senha: ")
            
        if senha != senha_verificacao:
            clear_terminal()
            print("\n\tAs senhas digitadas não coincidem, voltando ao menu principal...\n")
            self.menuPrincipal()
            quit()

        print(("Torce para o time do flamengo?"))
        isFlamengo = SimNao()
        if isFlamengo == "S" or isFlamengo == "SIM":
            isFlamengo = True
        else:
            isFlamengo = False

        self.registered(name, usuario, email, senha, isFlamengo)

    def bookSearch(self):
        search_c = ["D", "T", "A", "P", "F", "V", "VOLTAR"]
        print("\nAqui você consegue consultar os livros contidos no estoque da nossa livraria:\n")

        while True:
            p = input(
                    "* (D) Títulos disponíveis \n"
                    "* (T) Pesquisa por título \n"
                    "* (A) Pesquisa por autor \n"
                    "* (P) Pesquisa por ano de publicação \n"
                    "* (F) Pesquisa por faixa de preço \n\n"
                    "* (V) Voltar \n\n"
                    "-> "
                    )
            p = p.upper()

            if p not in search_c:
                print("\nDesculpe, tente novamente...\n")
                continue
            else:
                break

        self.pesquisa(p)

    def pesquisa(self, p):         
        if p == "D":
            self.pesquisaAmostra()

        elif p == "T":
            self.pesquisaTitulo()

        elif p == "A":
            self.pesquisaAutor()

        elif p == "P":
            self.pesquisaAnoPublicacao()

        elif p == "F":
            self.pesquisaFaixaPreco()

        elif p == "V" or p == "VOLTAR":
            clear_terminal()
            if self.logado:
                print("\nVoltando ao menu da sua conta...\n")
                self.menuUsuario()
            else:
                print("\nVoltando ao menu principal...\n")
                self.menuPrincipal()

        print("\n\nERRO!\n\n")
        quit()

    def pesquisaAmostra(self):
        table_livro = tables['livro']
        if (ret := table_livro.read_all('titulo')):

            clear_terminal()
            print(f"\nAlguns livros contidos no estoque da nossa livraria:")
            i = 0
            for row in ret:
                if i <=50:
                    i +=1
                    print(f" {i} - {row[0].capitalize()}")
                else:
                    print("...")
                    break

            if self.logado:
                print("\nDeseja adicionar ao seu carrinho de compras algum livro destacado acima?\n")
                comprar = SimNao()
                if comprar == "S" or comprar == "SIM":
                    index = input("\nInforme o índice do livro que deseja:\n-> ")
                    while not index.isnumeric() or int(index) <= 0 or int(index) > i:
                        index = input("\nPor favor informe um índice válido (número destacado a esquerda do título do livro):\n-> ")
                    self.adicionaLivro(ret[int(index) - 1][0])
                else:
                    clear_terminal()
                    print("\nCompra cancelada")
                    print("\nVoltando ao menu da sua conta...\n")
                    self.menuUsuario()
            else:
                print("\nDeseja fazer login e comprar algum livro destacado acima?\n")
                deseja = SimNao()
                if deseja == "S" or deseja == "SIM":
                    clear_terminal()
                    self.Login()
                else:
                    clear_terminal()
                    print("\nVoltando ao menu principal...\n")
                    self.menuPrincipal()
        else:
            clear_terminal()
            print("\nO estoque da livraria está vazio. Peça para algum funcionário atualizar o estoque.\n")
            
            Voltar()
            
            self.bookSearch()

    def pesquisaTitulo(self):
        clear_terminal()
        key_word = input(f"\nPor favor informe o titulo do livro desejado:\n-> ")
        Titulo = key_word
        table_livro = tables['livro']
        if (table_livro.read('titulo', titulo = Titulo, search_type = 'titulo')):
            if self.logado: # achou o livro e ta logado
                print("\nLivro encontrado, deseja adicioná-lo ao carrinho de compras?\n")
                comprar = SimNao()
                if comprar == "S" or comprar == "SIM":
                    self.adicionaLivro(Titulo)
                else:
                    clear_terminal()
                    print("\nCompra cancelada")
                    print("\nVoltando ao menu da sua conta...\n")
                    self.menuUsuario()
            else: # achou o livro e nao ta logado
                print("\nLivro encontrado, deseja fazer login para comprá-lo?\n")
                deseja = SimNao()
                if deseja == "S" or deseja == "SIM":
                    clear_terminal()
                    self.Login()
                else:
                    clear_terminal()
                    print("\nVoltando ao menu principal...\n")
                    self.menuPrincipal()
        else: # nao achou o livro
            print(f"\nNenhum livro no estoque da livraria possui o título '{Titulo.capitalize()}'.")
            if self.logado: # e ta logado
                print("\nVoltando ao menu da sua conta...\n")
                self.menuUsuario()
            else: # e nao ta logado
                print("\nVoltando ao menu principal...\n")
                self.menuPrincipal()

    def pesquisaAutor(self):
        key_word = input(f"\nPor favor informe o titulo do livro desejado:\n-> ")
        Autor = key_word
        table_livro = tables['livro']
        if (ret := table_livro.read('titulo', autor = Autor, search_type = 'autor')):

            clear_terminal()
            print(f"\nLivros escritos por {Autor}:")
            i = 0
            for row in ret:
                if i <=50:
                    i +=1
                    print(f" {i} - {row[0].capitalize()}")
                else:
                    print("...")
                    break

            if self.logado:
                print("\nDeseja adicionar ao seu carrinho de compras algum livro destacado acima?\n")
                comprar = SimNao()
                if comprar == "S" or comprar == "SIM":
                    index = input("\nInforme o índice do livro que deseja:\n-> ")
                    while not index.isnumeric() or int(index) <= 0 or int(index) > i:
                        index = input("\nPor favor informe um índice válido (número destacado a esquerda do título do livro):\n-> ")
                    
                    self.adicionaLivro(ret[int(index) - 1][0])
                else:
                    clear_terminal()
                    print("\nCompra cancelada")
                    print("\nVoltando ao menu da sua conta...\n")
                    self.menuUsuario()
            else:
                print("\nDeseja fazer login e comprar algum livro destacado acima?\n")
                deseja = SimNao()
                if deseja == "S" or deseja == "SIM":
                    clear_terminal()
                    self.Login()
                else:
                    clear_terminal()
                    print("\nVoltando ao menu principal...\n")
                    self.menuPrincipal()
        else:
            print(f"\nNenhum livro no estoque da livraria foi escrito por '{Autor.capitalize()}'.")
            if self.logado:
                print("\nVoltando ao menu da sua conta...\n")
                self.menuUsuario()
            else:
                print("\nVoltando ao menu principal...\n")
                self.menuPrincipal()

    def pesquisaAnoPublicacao(self):
        key_word = input("\nPor favor informe um número válido para o ano de publicação do livro:\n-> ")
        while not (key_word.isnumeric()) or int(key_word) >= 10000 or int(key_word) <= 0:
            key_word = input("\nPor favor informe um número válido para o ano de publicação do livro:\n-> ")
        anoPublicacao = key_word
        table_livro = tables['livro']
        if (ret := table_livro.read('titulo', ano_publicacao = anoPublicacao, search_type = 'ano_publicacao')):

            clear_terminal()
            print(f"\nLivros publicados no ano de {anoPublicacao}:")
            i = 0
            for row in ret:
                if i <=50: # pra mostrar só os 50 primeiros livros
                    i+=1
                    print(f" {i} - {row[0].capitalize()}")
                else:
                    print("...")
                    break

            if self.logado:
                print("\nDeseja adicionar ao seu carrinho de compras algum livro destacado acima?\n")
                comprar = SimNao()
                if comprar == "S" or comprar == "SIM":
                    index = input("\nInforme o índice do livro que deseja:\n-> ")
                    while not index.isnumeric() or int(index) <= 0 or int(index) > i:
                        index = input("\nPor favor informe um índice válido (número destacado a esquerda do título do livro):\n-> ")
                    self.adicionaLivro(ret[int(index) - 1][0])
                else:
                    clear_terminal()
                    print("\nCompra cancelada")
                    print("\nVoltando ao menu da sua conta...\n")
                    self.menuUsuario()
            else:
                print("\nDeseja fazer login e comprar algum livro destacado acima?\n")
                deseja = SimNao()
                if deseja == "S" or deseja == "SIM":
                    clear_terminal()
                    self.Login()
                else:
                    clear_terminal()
                    print("\nVoltando ao menu principal...\n")
                    self.menuPrincipal()
        else:
            print(f"\nNenhum livro no estoque da livraria foi publicado no ano de {anoPublicacao}.")
            if self.logado:
                print("\nVoltando ao menu da sua conta...\n")
                self.menuUsuario()
            else:
                print("\nVoltando ao menu principal...\n")
                self.menuPrincipal()

    def pesquisaFaixaPreco(self):
        min_value = input("\nBuscar livros acima de R$")
        while not (min_value.isnumeric()) or int(min_value) >= 10000 or int(min_value) < 0:
            min_value = input("\nPor favor informe um valor válido para a busca:\n-> R$ ")

        max_value = input("\nBuscar livros abaixo de R$")
        while not (max_value.isnumeric()) or int(min_value) >= 10000 or int(min_value) < 0:
            max_value = input("\nPor favor informe um valor válido para a busca:\n-> R$ ")

        table_livro = tables['livro']
        if (ret := table_livro.query(f'SELECT titulo FROM livro WHERE preco >= {min_value} and preco <= {max_value}')):

            clear_terminal()
            print(f"\nLivros com preço entre R${min_value} e R${max_value}:")
            i = 0
            for row in ret:
                if i <=50: # pra mostrar só os 50 primeiros livros
                    i+=1
                    print(f" {i} - {row[0].capitalize()}")
                else:
                    print("...")
                    break

            if self.logado:
                print("\nDeseja adicionar ao seu carrinho de compras algum livro destacado acima?\n")
                comprar = SimNao()
                if comprar == "S" or comprar == "SIM":
                    index = input("\nInforme o índice do livro que deseja:\n-> ")
                    while not index.isnumeric() or int(index) <= 0 or int(index) > i:
                        index = input("\nPor favor informe um índice válido (número destacado a esquerda do título do livro):\n-> ")
                    self.adicionaLivro(ret[int(index) - 1][0])
                else:
                    clear_terminal()
                    print("\nCompra cancelada")
                    print("\nVoltando ao menu da sua conta...\n")
                    self.menuUsuario()
            else:
                print("\nDeseja fazer login e comprar algum livro destacado acima?\n")
                deseja = SimNao()
                if deseja == "S" or deseja == "SIM":
                    clear_terminal()
                    self.Login()
                else:
                    clear_terminal()
                    print("\nVoltando ao menu principal...\n")
                    self.menuPrincipal()
        else:
            clear_terminal()
            print(f"\nNenhum livro no estoque da livraria está entre nessa faixa de preço mencionada.")
            if self.logado:
                print("\nVoltando ao menu da sua conta...\n")
                self.menuUsuario()
            else:
                print("\nVoltando ao menu principal...\n")
                self.menuPrincipal()
        
    def menuCarrinho(self):
        search_c = ["A", "R", "C", "F", "E", "V", "VOLTAR"]
        print("\n\tCarrinho de compras\n")

        while True:
            p = input(
                    "* (A) Adicionar livro \n"
                    "* (R) Remover livro \n"
                    "* (C) Ver livros no carrinho \n"
                    "* (F) Continuar para o pagamento \n"
                    "* (E) Esvaziar carrinho de compras \n\n"
                    "* (V) Voltar \n\n"
                    "-> "
                    )
            p = p.upper()

            if p not in search_c:
                print("\nDesculpe, tente novamente...\n")
                continue
            else:
                break

        if p == "A":
            clear_terminal()
            self.bookSearch()

        elif p == "R":
            self.removeLivro()

        elif p == "C":
            self.verCarrinho()

        elif p == "F":
            self.compra()

        elif p == "E":
            self.esvaziaCarrinho()

        elif p == "V" or p == "VOLTAR":
            clear_terminal()
            if self.logado:
                print("\nVoltando ao menu da sua conta...\n")
                self.menuUsuario()
            else:
                print("\nVoltando ao menu principal...\n")
                self.menuPrincipal()

        print("\n\nERRO!\n\n")
        quit()

    def adicionaLivro(self, titulo_a_adicionar):
        livros = tables['livro']
        clientes = tables['cliente']
        carrinho = tables['carrinho']
        itens_carrinho = tables['item_carrinho']
        
        idCliente = clientes.read('id_cliente', usuario = self.usuario_logado, search_type = 'usuario')[0][0]
        idCarrinho = carrinho.read('id_carrinho', id_cliente = idCliente, search_type = 'id_cliente')[0][0]
        idLivro = livros.read('id_livro', titulo = titulo_a_adicionar, search_type = 'titulo')[0][0]
        
        itens_carrinho.insert(id_carrinho = idCarrinho, id_livro = idLivro)
        
        print("\nLivro adicionado ao seu carrinho de compras.")
        
        print("\nDeseja ir para o pagamento?\n-> ")
        escolha = SimNao()
        if escolha == "S" or escolha == "SIM":
            self.compra()
        else:
            clear_terminal()
            print("\nVoltando ao menu da sua conta...\n")
            self.menuUsuario()

    def removeLivro(self):
        clear_terminal()
        livros = tables['livro']
        clientes = tables['cliente']
        carrinho = tables['carrinho']
        itens_carrinho = tables['item_carrinho']
        
        idCliente = clientes.read('id_cliente', usuario = self.usuario_logado, search_type = 'usuario')[0][0]
        id_carrinho_do_cliente = carrinho.read('id_carrinho', id_cliente = idCliente, search_type = 'id_cliente')[0][0]
        id_livros_carrinho = itens_carrinho.read('id_livro', id_carrinho = id_carrinho_do_cliente, search_type = 'id_carrinho')

        if not (itens_carrinho.read('*', id_carrinho = id_carrinho_do_cliente, search_type = 'id_cliente')):
            clear_terminal()
            print("\nSeu carrinho de compras está vazio.")
            print("\nVoltando...")
            self.menuCarrinho()
        
        print(f"\n\tLivros no seu carrinho de compras:\n")
        i = 0
        for i in range(len(id_livros_carrinho)):
            titulo_no_carrinho = livros.read('titulo', id_livro = id_livros_carrinho[i][0], search_type = 'id_livro')[0][0]
            if i <=50:
                print(f" {i + 1} - {titulo_no_carrinho.capitalize()}")
            else:
                print("...")
                break

        index = input("\nInforme o índice do livro que deseja remover:\n-> ")
        while not index.isnumeric() or int(index) <= 0 or int(index) > i + 1:
            index = input("\nPor favor informe um índice válido (número destacado a esquerda do título do livro):\n-> ")

        idLivroRemover = id_livros_carrinho[int(index)-1][0]
        idItemRemover = itens_carrinho.read('id_item_carrinho', id_livro = idLivroRemover, search_type = 'id_livro')
        itens_carrinho.deleteItem(id_item_carrinho = idItemRemover[0][0], delete_type = 'id_item_carrinho')

        print("\nLivro removido do carrinho de compras.")
        
        print("\nDeseja remover outro livro?")
        escolha = SimNao()
        if escolha == "S" or escolha == "SIM":
            self.removeLivro()
        else:
            clear_terminal()
            print("\nVoltando...")
            self.menuCarrinho()
    
    def verCarrinho(self):
        clear_terminal()
        livros = tables['livro']
        clientes = tables['cliente']
        carrinho = tables['carrinho']
        itens_carrinho = tables['item_carrinho']
        
        idCliente = clientes.read('id_cliente', usuario = self.usuario_logado, search_type = 'usuario')[0][0]
        id_carrinho_do_cliente = carrinho.read('id_carrinho', id_cliente = idCliente, search_type = 'id_cliente')[0][0]

        if not (itens_carrinho.read('*', id_carrinho = id_carrinho_do_cliente, search_type = 'id_cliente')):
            clear_terminal()
            print("\nSeu carrinho de compras está vazio.")
            print("\nVoltando...")
            self.menuCarrinho()
        else:
            clear_terminal()
            id_livros_carrinho = itens_carrinho.read('id_livro', id_carrinho = id_carrinho_do_cliente, search_type = 'id_carrinho')
            
            print(f"\n\tLivros no seu carrinho de compras:\n")
            for i in range(len(id_livros_carrinho)):
                titulo_no_carrinho = livros.read('titulo', id_livro = id_livros_carrinho[i][0], search_type = 'id_livro')[0][0]
                if i <=50:
                    print(f" {i + 1} - {titulo_no_carrinho.capitalize()}")
                else:
                    print("...")
                    break
            
            Voltar()
            print("\nVoltando...")
            self.menuCarrinho()
    
    def compra(self):
        clear_terminal()
        livros = tables['livro']
        clientes = tables['cliente']
        carrinho = tables['carrinho']
        itens_carrinho = tables['item_carrinho']
        
        idCliente = clientes.read('id_cliente', usuario = self.usuario_logado, search_type = 'usuario')[0][0]
        id_carrinho_do_cliente = carrinho.read('id_carrinho', id_cliente = idCliente, search_type = 'id_cliente')[0][0]
        id_livros_carrinho = itens_carrinho.read('id_livro', id_carrinho = id_carrinho_do_cliente, search_type = 'id_carrinho')
        
        if not (itens_carrinho.read('*', id_carrinho = id_carrinho_do_cliente, search_type = 'id_cliente')):
            print("\nSeu carrinho de compras já está vazio.")
            print("\nVoltando...")
            self.menuCarrinho()
        else:
            print(f"\n\tLivros no seu carrinho de compras:\n")
            custo_total = 0
            for i in range(len(id_livros_carrinho)):
                titulo_no_carrinho = livros.read('titulo', id_livro = id_livros_carrinho[i][0], search_type = 'id_livro')[0][0]
                preco_no_carrinho = livros.read('preco', id_livro = id_livros_carrinho[i][0], search_type = 'id_livro')[0][0]
                custo_total+=preco_no_carrinho
                if i <=50:
                    print(f" R${preco_no_carrinho} - {titulo_no_carrinho.capitalize()}")
                else:
                    print("...")
                    break
            
            print(f"\nConfirmar compra no valor total de R${custo_total:.2f}?")
            deseja = SimNao()
            
            if deseja == "S" or deseja == "SIM":
                flamenguista = clientes.read('isFlamengo', usuario = self.usuario_logado, search_type = 'usuario')[0][0]
                if flamenguista:
                    print("\nVocê ganhou um desconto de 15% na compra por torcer para o time do Flamengo.")
                    custo_total = custo_total * (1 - 0.15)
                    print(f"Valor após o desconto -> R${custo_total:.2f}")
                    
                print(f"\nProcessando pagamento...")
                
                pedidos = tables['pedido']
                pedidos.insert(id_cliente = idCliente, custo = round(custo_total, 2))
                
                idPedidoCliente = pedidos.read('id_pedido', id_cliente = idCliente, search_type = 'usuario')[-1][0]
                itens_pedidos = tables['item_pedido']
                for i in range(len(id_livros_carrinho)):
                    itens_pedidos.insert(id_pedido = idPedidoCliente, id_livro = id_livros_carrinho[i][0])

                print(f"Compra autorizada no valor de R$ {custo_total:.2f}.")
                print("\nSeus livros podem ser visualizados na aba de pedidos no menu de sua conta.")
                
                print(f"\nAperte enter para continuar.")
                input()
                self.esvaziaCarrinho()

                Voltar()                
                print("\nVoltando ao menu da sua conta...")
                self.menuUsuario()
            else:
                clear_terminal()
                print("\nCompra cancelada")
                print("\nVoltando ao menu da sua conta...")
                self.menuUsuario()

    def esvaziaCarrinho(self):
        clear_terminal()
        clientes = tables['cliente']
        carrinho = tables['carrinho']
        itens_carrinho = tables['item_carrinho']

        idCliente = clientes.read('id_cliente', usuario = self.usuario_logado, search_type = 'usuario')[0][0]
        id_carrinho_do_cliente = carrinho.read('id_carrinho', id_cliente = idCliente, search_type = 'id_cliente')[0][0]

        if (itens_carrinho.read('*', id_carrinho = id_carrinho_do_cliente, search_type = 'id_cliente')):
            itens_carrinho.deleteAll(id_carrinho = id_carrinho_do_cliente)

            clear_terminal()
            print("\n\tCarrinho de compras esvaziado.")
            print("\nVoltando...")
            self.menuCarrinho()
        else:
            print("\nSeu carrinho de compras já está vazio.")
            print("\nVoltando...")
            self.menuCarrinho()

    def verDadosCadastrais(self):
        clear_terminal()
        clientes = tables['cliente']
        
        nomeCliente = clientes.read('nome', usuario = self.usuario_logado, search_type ='usuario')[0][0]
        usuarioCliente = clientes.read('usuario', usuario = self.usuario_logado, search_type ='usuario')[0][0]
        emailCliente = clientes.read('email', usuario = self.usuario_logado, search_type ='usuario')[0][0]

        print("\nAqui estão as informações da sua conta:\n")
        print(f"- Nome: {nomeCliente}")
        print(f"- Usuário: {usuarioCliente}")
        print(f"- Email: {emailCliente}")

            
        Voltar()
        print("\nVoltando ao menu da sua conta...")
        self.menuUsuario()

    def verPedidos(self):
        clear_terminal()
        livros = tables['livro']
        clientes = tables['cliente']
        pedidos = tables['pedido']
        itens_pedido = tables['item_pedido']

        print(f"\n\tHistórico de pedidos:\n")
        
        idCliente = clientes.read('id_cliente', usuario = self.usuario_logado, search_type = 'usuario')[0][0]
        idPedidosCliente = pedidos.read('id_pedido', id_cliente = idCliente, search_type = 'id_cliente')
        if (idPedidosCliente):
            
            for i in range(len(idPedidosCliente)):
                idItensPedidos = itens_pedido.read('id_livro', id_pedido = idPedidosCliente[i][0], search_type = 'id_pedido')
                print(f"ID do pedido: {idPedidosCliente[i][0]}")
                
                for j in range(len(idItensPedidos)):
                    titulo = livros.read('titulo', id_livro = idItensPedidos[j][0], search_type = 'id_livro')[0][0]
                    preco = livros.read('preco', id_livro = idItensPedidos[j][0], search_type = 'id_livro')[0][0]
                    flamenguista = clientes.read('isFlamengo', usuario = self.usuario_logado, search_type = 'usuario')[0][0]
                    if flamenguista:
                        preco = preco * (1 - 0.15)
                    print(f"\tR${preco:.2f} - {titulo.capitalize()}")
                    
                print("-----------------------------------")
                total_pedido = pedidos.read('custo', id_pedido = idPedidosCliente[i][0], search_type = 'id_pedido')[0][0]
                print(f"\tPreço total: R${total_pedido:.2f}\n\n")

        else:
            print("\nVocê ainda não tem nenhum pedido registrado.")

        Voltar()
        print("\nVoltando ao menu da sua conta...")
        self.menuUsuario()

    def mostra_clientes(self):
        clear_terminal()
        clientes = tables['cliente']
        nomes = clientes.read_all('nome')
        if nomes:
            print("\nClientes cadastrados na livraria:\n")
            i = 0
            for row in nomes:
                if i <=50: # pra mostrar só os 50 primeiros clientes
                    i+=1
                    print(f"Cliente {i} - {row[0]}")
                else:
                    print("...")
                    break
        else:
            print("\nNão há nenhum cliente cadastrado ainda.")

        Voltar()
        print("\nVoltando ao menu principal...\n")
        self.menuPrincipal()

    def mostra_vendas(self):
        clear_terminal()
        clientes = tables['cliente']
        pedidos = tables['pedido']
        vendas = pedidos.read_all('id_pedido, custo, id_cliente')
        if vendas:
            print("\nVendas registradas na livraria:\n")
            i = 0
            for row in vendas:
                if i <=50: # pra mostrar só as 50 primeiras vendas
                    i+=1
                    nomeCliente = clientes.read('nome', id_cliente = row[2], search_type = 'id_cliente')[0][0]
                    print(f"Venda {row[0]} - R${row[1]:.2f}  - {nomeCliente}")
                else:
                    print("...")
                    break
        else:
            print("\nNão há nenhuma venda registrada ainda.")

        Voltar()
        print("\nVoltando ao menu principal...\n")
        self.menuPrincipal()
