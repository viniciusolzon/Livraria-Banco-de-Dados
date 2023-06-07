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
            self.carrinho()
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
        clear_terminal()
        print("\n\tRegistro feito com sucesso!\n")
        self.menuPrincipal()
        quit()

    def Login(self):
        print("\n\t#####################"
                "\t### Tela de Login ###"
                "\t#####################")
            
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
        print("\n\t######################"
                "  ### Tela de Cadastro ###  "
                "######################")
            
        # aqui não precisa de verificação nenhuma pq podem existir vários usuários com o mesmo nome
        name = input("\n\tNome completo: ")

        email = input("\tEmail: ")
        if(not checkEmail(email)):
            print("\n\tO email inserido já possui cadastro na livraria, voltando ao menu principal...\n")
            self.menuPrincipal()
            quit()

        usuario = input("\tNome de usuário: ")
        if(not checkUsername(usuario)):
            print("\n\tEsse nome de usuário já possui cadastro na livraria, voltando ao menu principal...\n")
            self.menuPrincipal()
            quit()

        senha = input("\tSenha: ")
        senha_verificacao = input("\tVerificação da senha: ")
        
        if senha != senha_verificacao:
            print("\n\tAs senhas digitadas não coincidem, por favor tente novamente:")
            senha = input("\tSenha: ")
            senha_verificacao = input("\tVerificação da senha: ")
            
        if senha != senha_verificacao:
            clear_terminal()
            print("\n\tAs senhas digitadas não coincidem, voltando ao menu principal...\n")
            self.menuPrincipal()
            quit()

        print(("\tÉ flamenguista?"))
        isFlamengo = SimNao()
        if isFlamengo == "S" or isFlamengo == "SIM":
            isFlamengo = True
        else:
            isFlamengo = False

        self.registered(name, usuario, email, senha, isFlamengo)

    def bookSearch(self):
        search_c = ["D", "T", "A", "P", "V", "VOLTAR"]
        print("\nAqui você consegue consultar os livros contidos no estoque da nossa livraria:\n")

        while True:
            p = input(
                    "* (D) Títulos disponíveis \n"
                    "* (T) Pesquisa por título \n"
                    "* (A) Pesquisa por autor \n"
                    "* (P) Pesquisa por ano de publicação \n\n"
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

    def pesquisaAmostra(self):
        table_livro = tables['livro']
        if (ret := table_livro.read_all('titulo')):

            clear_terminal()
            print(f"\nAlguns livros contidos no estoque da nossa livraria:")
            i = 0
            for row in ret:
                if i <=50:
                    i +=1
                    print(f" {i} - {row[0]}")
                else:
                    print("...")
                    break

            if self.logado:
                print("\nDeseja comprar algum livro destacado acima?\n")
                comprar = SimNao()
                if comprar == "S" or comprar == "SIM":
                    index = input("\nInforme o índice do livro que deseja comprar dentre os que estão destacado acima:\n-> ")
                    while not index.isnumeric() or int(index) <= 0 or int(index) > i:
                        index = input("\nPor favor informe um índice válido (número destacado a esquerda do título do livro):\n-> ")
                    self.compra(ret[int(index) - 1][0])
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
                print("\nLivro encontrado, deseja comprá-lo?\n")
                comprar = SimNao()
                if comprar == "S" or comprar == "SIM":
                    self.compra(Titulo)
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
            print(f"\nNenhum livro no estoque da livraria possui o título '{Titulo}'.")
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
                    print(f" {i} - {row[0]}")
                else:
                    print("...")
                    break

            if self.logado:
                print("\nDeseja comprar algum livro destacado acima?\n")
                comprar = SimNao()
                if comprar == "S" or comprar == "SIM":
                    index = input("\nInforme o índice do livro que deseja comprar dentre os que estão destacado acima:\n-> ")
                    while not index.isnumeric() or int(index) <= 0 or int(index) > i:
                        index = input("\nPor favor informe um índice válido (número destacado a esquerda do título do livro):\n-> ")
                    
                    self.compra(ret[int(index) - 1][0])
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
            print(f"\nNenhum livro no estoque da livraria foi escrito por '{Autor}'.")
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
                    print(f" {i} - {row[0]}")
                else:
                    print("...")
                    break

            if self.logado:
                print("\nDeseja comprar algum livro destacado acima?\n")
                comprar = SimNao()
                if comprar == "S" or comprar == "SIM":
                    index = input("\nInforme o índice do livro que deseja comprar dentre os que estão destacado acima:\n-> ")
                    while not index.isnumeric() or int(index) <= 0 or int(index) > i:
                        index = input("\nPor favor informe um índice válido (número destacado a esquerda do título do livro):\n-> ")
                    self.compra(ret[int(index) - 1][0])
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

    def pesquisa(self, p):         
        if p == "D":
            self.pesquisaAmostra()

        elif p == "T":
            self.pesquisaTitulo()

        elif p == "A":
            self.pesquisaAutor()

        elif p == "P":
            self.pesquisaAnoPublicacao()

        elif p == "V" or p == "VOLTAR":
            clear_terminal()
            if self.logado:
                print("\nVoltando ao menu da sua conta...\n")
                self.menuUsuario()
            print("\nVoltando ao menu principal...\n")
            self.menuPrincipal()

        print("\n\nERRO!\n\n")
        quit()
        
    def carrinho(self):
        clear_terminal()
        search_c = ["A", "R", "F", "E", "V", "VOLTAR"]
        print("\n\tCarrinho de compras\n")

        while True:
            p = input(
                    "* (A) Adicionar livro \n"
                    "* (R) Remover livro \n"
                    "* (L) Ver livros no carrinho \n"
                    "* (F) Finalizar compra \n"
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
            self.pesquisaTitulo()

        elif p == "L":
            self.pesquisaTitulo()

        elif p == "F":
            self.pesquisaAutor()

        elif p == "E":
            self.pesquisaAnoPublicacao()

        elif p == "V" or p == "VOLTAR":
            clear_terminal()
            if self.logado:
                print("\nVoltando ao menu da sua conta...\n")
                self.menuUsuario()
            print("\nVoltando ao menu principal...\n")
            self.menuPrincipal()

        print("\n\nERRO!\n\n")
        quit()

    def compra(self, Titulo):
        # self.carrinho(Titulo)
        
        livros = tables['livro']
        clientes = tables['cliente']
        pedidos = tables['pedido']

        idCliente = clientes.read('id_cliente', usuario = self.usuario_logado, search_type = 'usuario')[0][0]
        idLivro = livros.read('id_livro', titulo = Titulo, search_type = 'titulo')[0][0]
        preco = livros.read('preco', titulo = Titulo, search_type = 'titulo')[0][0]

        clear_terminal()
        print(f"\nConfirmar compra do livro '{Titulo}' no valor {preco:.2f}?")
        deseja = SimNao()
        
        flamenguista = clientes.read('isFlamengo', usuario = self.usuario_logado, search_type = 'usuario')[0][0]
        
        if deseja == "S" or deseja == "SIM":
            if flamenguista:
                print("\nParabéns, você acaba de ganhar um desconto de 15% nessa compra por ser flamenguista.")
                preco = preco * (1 - 0.15)
            
            print(f"\nProcessando pagamento...")
            print(f"Compra autorizada no valor de R$ {preco:.2f}.")
            
            pedidos.insert(id_cliente = idCliente, id_livro = idLivro, custo = preco)
            
            print("Livro comprado!")
            print("\nSeu livro agora pode ser visualizado na aba de pedidos no menu de sua conta.")

            Voltar()
                
            print("\nVoltando ao menu da sua conta...")
            
            self.menuUsuario()
        else:
            clear_terminal()
            print("\nCompra cancelada")
            print("\nVoltando ao menu da sua conta...")
            self.menuUsuario()

    def verDadosCadastrais(self):
        clear_terminal()
        clientes = tables['cliente']
        
        nomeCliente = clientes.read('nome', usuario = self.usuario_logado, search_type='usuario')[0][0]
        usuarioCliente = clientes.read('usuario', usuario = self.usuario_logado, search_type='usuario')[0][0]
        emailCliente = clientes.read('email', usuario = self.usuario_logado, search_type='usuario')[0][0]

        print("\nAqui estão as informações da sua conta:\n")
        print(f"- Nome: {nomeCliente}")
        print(f"- Usuário: {usuarioCliente}")
        print(f"- Email: {emailCliente}")

            
        Voltar()
        print("\nVoltando ao menu da sua conta...")
        self.menuUsuario()

    def verPedidos(self):
        clear_terminal()
        clientes = tables['cliente']

        idCliente = clientes.read('id_cliente', usuario = self.usuario_logado, search_type='usuario')[0][0]
        if(idLivro := clientes.query(f"SELECT id_livro FROM pedido WHERE {idCliente} = pedido.id_cliente")):
            print(f"\nHistórico dos pedidos de {self.usuario_logado}:\n")
            qtd_pedidos = clientes.query(f"SELECT COUNT (id_livro) FROM pedido WHERE {idCliente} = pedido.id_cliente")[0][0]
            i = 0
            for i in range (qtd_pedidos):
                titulo = clientes.query(f"SELECT titulo FROM livro WHERE {idLivro[i][0]} = livro.id_livro")[0][0]
                # print(titulo)
                preco = clientes.query(f"SELECT custo FROM pedido WHERE {idCliente} = pedido.id_cliente")[i][0]
                # print(preco)
                print(f" {i+1} - {titulo} | R$ {preco:.2f}")    
            if i>=50:
                print("...")
            
        else:
            print("\nVocê ainda não fez nenhum pedido.")
            Voltar()

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

        Voltar()
        print("\nVoltando ao menu principal...\n")
        self.menuPrincipal()

    def mostra_vendas(self):
        clear_terminal()
        pedidos = tables['pedido']
        vendas = pedidos.read_all('id_pedido, custo')
        if vendas:
            print("\nVendas registradas na livraria:\n")
            i = 0
            for row in vendas:
                if i <=50: # pra mostrar só as 50 primeiras vendas
                    i+=1
                    print(f"Venda {row[0]} - R$ {row[1]:.2f}")
                else:
                    print("...")
                    break
        else:
            print("\nNão há nenhuma venda registrada ainda.")
            Voltar()

        Voltar()
        print("\nVoltando ao menu principal...\n")
        self.menuPrincipal()
