import sqlite3

# Conectar ao banco de dados (cria o banco se não existir)
conn = sqlite3.connect('exercicio_banco_dados.db')
cursor = conn.cursor()

# Exercício Gerenciamento de Mercado 
# 1. Criação das Tabelas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Produtos (
        ProdutoID INTEGER PRIMARY KEY,
        Nome TEXT,
        Categorias TEXT,
        QuantidadeEstoque INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Fornecedores (
        FornecedorID INTEGER PRIMARY KEY,
        Nome TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ProdutoFornecedor (
        ProdutoID INTEGER,
        FornecedorID INTEGER,
        FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID),
        FOREIGN KEY (FornecedorID) REFERENCES Fornecedores(FornecedorID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clientes (
        ClienteID INTEGER PRIMARY KEY,
        Nome TEXT,
        Telefone TEXT,
        Endereco TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Transacoes (
        TransacaoID INTEGER PRIMARY KEY,
        ClienteID INTEGER,
        ProdutoID INTEGER,
        Quantidade INTEGER,
        DataCompra DATE,
        FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID),
        FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID)
    )
''')

# 2. Inserção de Dados
cursor.execute("INSERT INTO Produtos VALUES (1, 'Produto A', 'Eletrônicos', 20)")
cursor.execute("INSERT INTO Produtos VALUES (2, 'Produto B', 'Alimentos', 30)")

cursor.execute("INSERT INTO Fornecedores VALUES (1, 'Fornecedor X')")
cursor.execute("INSERT INTO Fornecedores VALUES (2, 'Fornecedor Y')")

cursor.execute("INSERT INTO ProdutoFornecedor VALUES (1, 1)")
cursor.execute("INSERT INTO ProdutoFornecedor VALUES (2, 2)")

cursor.execute("INSERT INTO Clientes VALUES (1, 'Cliente 1', '987654321', 'Rua B, 456')")

cursor.execute("INSERT INTO Transacoes VALUES (1, 1, 10, '2024-02-10')")
cursor.execute("INSERT INTO Transacoes VALUES (1, 2, 5, '2024-02-15')")

# 3. Consultas SQL
# Listar todos os produtos em estoque
cursor.execute("SELECT * FROM Produtos")
print("\nProdutos em Estoque:")
print(cursor.fetchall())

# Encontrar as vendas realizadas por um cliente específico
cursor.execute("SELECT * FROM Transacoes WHERE ClienteID = 1")
print("\nVendas realizadas pelo Cliente 1:")
print(cursor.fetchall())

# Calcular o total de vendas por categoria de produto
cursor.execute("SELECT Categorias, SUM(Quantidade) FROM Produtos JOIN Transacoes ON Produtos.ProdutoID = Transacoes.ProdutoID GROUP BY Categorias")
print("\nTotal de Vendas por Categoria:")
print(cursor.fetchall())

# Identificar os produtos mais vendidos
cursor.execute("SELECT Produtos.Nome, SUM(Quantidade) FROM Produtos JOIN Transacoes ON Produtos.ProdutoID = Transacoes.ProdutoID GROUP BY Produtos.Nome ORDER BY SUM(Quantidade) DESC")
print("\nProdutos Mais Vendidos:")
print(cursor.fetchall())

# 4. Atualizações e Exclusões (exemplo: atualizar a quantidade em estoque após uma venda)
cursor.execute("UPDATE Produtos SET QuantidadeEstoque = QuantidadeEstoque - 5 WHERE ProdutoID = 2")

# Salvar as alterações e fechar a conexão
conn.commit()
conn.close()
