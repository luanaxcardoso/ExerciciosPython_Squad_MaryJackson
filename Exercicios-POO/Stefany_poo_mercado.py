# Classe Fornecedor: Representa um fornecedor de produtos
class Fornecedor:
    def __init__(self, nome):
        self.nome = nome

# Classe Produto: Representa um produto no mercado
class Produto:
    def __init__(self, nome, categorias, quantidade_estoque):
        self.nome = nome
        self.categorias = categorias
        self.quantidade_estoque = quantidade_estoque
        self.fornecedores = []

    def adicionar_fornecedor(self, fornecedor):
        # Método para adicionar fornecedor ao produto
        self.fornecedores.append(fornecedor)

# Classe Cliente: Representa um cliente do mercado
class Cliente:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

# Classe Mercado: Representa o mercado e suas operações
class Mercado:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.clientes = []
        self.produtos = []
        self.transacoes = []

    def cadastrar_cliente(self, cliente):
        # Método para cadastrar um novo cliente no mercado
        self.clientes.append(cliente)

    def cadastrar_produto(self, produto):
        # Método para cadastrar um novo produto no mercado
        self.produtos.append(produto)

    def realizar_compra(self, cliente, produto, quantidade, data_compra):
        # Método para realizar a compra de produtos por um cliente
        # Aqui você implementaria a lógica, como verificar o estoque, calcular o total, etc.
        pass

# Exemplo de Uso:
fornecedor1 = Fornecedor("Fornecedor A")
produto1 = Produto("Produto 1", ["Alimentos", "Bebidas"], 50)
produto1.adicionar_fornecedor(fornecedor1)

cliente1 = Cliente("Cliente 1", "987654321", "Rua A, 123")

mercado = Mercado("Mercado Central", "123456789")
mercado.cadastrar_cliente(cliente1)
mercado.cadastrar_produto(produto1)
