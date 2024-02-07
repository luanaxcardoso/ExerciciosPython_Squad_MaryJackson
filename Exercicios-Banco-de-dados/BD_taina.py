import sqlite3
from datetime import datetime

conexao = sqlite3.connect('bancodbeaver') 
cursor = conexao.cursor()


#Criando as tabelas
cursor.execute('CREATE TABLE Estoque(idProduto INT PRIMARY KEY, produto VARCHAR(100), categoria VARCHAR(100), estoque INT, preço REAL, fornecedores VARCHAR(100) )')
cursor.execute('CREATE TABLE Clientes(idCliente INT PRIMARY KEY, cliente VARCHAR(100), telefone INT, endereço VARCHAR(100), idProduto INT, quantidade INT )')
cursor.execute('CREATE TABLE Saída(idSaida INT PRIMARY KEY, idCliente INT, idProduto INT, quantidade INT, conta INT, data TIMESTAMP, FOREIGN KEY (idProduto) REFERENCES Estoque(idProduto),FOREIGN KEY (idCliente) REFERENCES Clientes(idCliente))') #relaciona as quantidades de saidas com o estoque e dados do cliente


#Preenchendo automaticamente a tabela de Saída
cursor.execute('''
    #CREATE TRIGGER inserir_saida AFTER INSERT ON Clientes
    #BEGIN
        #INSERT INTO Saída (idCliente, idProduto, quantidade, conta, data)
        #SELECT NEW.idCliente, NEW.idProduto, NEW.quantidade, (NEW.quantidade * Estoque.preço), CURRENT_TIMESTAMP
        #FROM Estoque
        #WHERE Estoque.idProduto = NEW.idProduto;
    #END;
''')


#Inserindo itens
cursor.execute('INSERT INTO Estoque(idProduto, produto, categoria, estoque, preço, fornecedores) VALUES (1, "Samsung S20E", "Celular", 35, 1290, "Ibyte")')
cursor.execute('INSERT INTO Estoque(idProduto, produto, categoria, estoque, preço, fornecedores) VALUES (2, "Samsung A34", "Celular", 10, 1100, "Casas Bahia")')
cursor.execute('INSERT INTO Estoque(idProduto, produto, categoria, estoque, preço, fornecedores) VALUES (3, "moto g84", "Celular", 22, 1120, "MagaLu")')
cursor.execute('INSERT INTO Estoque(idProduto, produto, categoria, estoque, preço, fornecedores) VALUES (4, "Smart TV 43 LG", "Televisores", 13, 1566, "Americanas; Casas Bahia")')
cursor.execute('INSERT INTO Estoque(idProduto, produto, categoria, estoque, preço, fornecedores) VALUES (5, "PlayStation5", "Video Game", 3, 3700, "Amazon")')


#Inserindo clientes 
cursor.execute('INSERT INTO Clientes(idCliente, cliente, telefone, endereço, idProduto, quantidade) VALUES (1, "João", 85914627855, "R.São José, 12", 4, 2 )')
cursor.execute('INSERT INTO Clientes(idCliente, cliente, telefone, endereço, idProduto, quantidade) VALUES (2, "Marcelo", 45965712225, "R. Das Graças, 410", 5, 1 )')
cursor.execute('INSERT INTO Clientes(idCliente, cliente, telefone, endereço, idProduto, quantidade) VALUES (3, "Vivian", 85954236156, "Av. Contorno Leste, 231", 3, 1 )')
cursor.execute('INSERT INTO Clientes(idCliente, cliente, telefone, endereço, idProduto, quantidade) VALUES (4, "Júlia", 85942111743, "R. Matos Dourados, 123", 5, 2 )')
cursor.execute('INSERT INTO Clientes(idCliente, cliente, telefone, endereço, idProduto, quantidade) VALUES (5, "Antonela", 11755561476, "Av. da Universidade, 456", 4, 1)')
cursor.execute('INSERT INTO Clientes(idCliente, cliente, telefone, endereço, idProduto, quantidade) VALUES (6, "jesuita", 18955545548, "Av. 13 de Maio, 4587", 1, 2)')
cursor.execute('INSERT INTO Clientes(idCliente, cliente, telefone, endereço, idProduto, quantidade) VALUES (7, "Maria", 86914644855, "R.São Marcos, 113", 4, 1 )')


#Listar todos os produtos em estoque.
dados = cursor.execute('SELECT produto FROM Estoque') 
for Estoque in dados:
    print(Estoque)


#Encontrar as vendas realizadas por um cliente específico, escolhi a cliente Maria de idCliente =7
dados = cursor.execute('SELECT idProduto FROM Saída WHERE idCliente=7') 
for idProduto in dados:
    idProduto = idProduto[0]
    if idProduto == 1:
        print("Samsung S20E")
    elif idProduto == 2:
        print("Samsung A34")
    elif idProduto == 3:
        print("moto g84")
    elif idProduto == 4:
        print("Smart TV 43 LG")
    elif idProduto == 5:
        print("PlayStation5")
    else:
        print("Não encontrado o histórico de vendas desse cliente.")


#Calcular o total de vendas por categoria de produto.
cursor.execute('''
    SELECT Estoque.categoria, SUM(Saída.quantidade)
    FROM Saída
    JOIN Estoque ON Saída.idProduto = Estoque.idProduto
    GROUP BY Estoque.categoria
''')
for categoria, total in cursor:
    print("Categoria:", categoria)
    print("Total de Vendas:", total)


#Identificar os produtos mais vendidos.
dados = cursor.execute('SELECT idProduto FROM Saída ORDER BY quantidade')
for idProduto in dados:
    idProduto = idProduto[0]
    if idProduto == 1:
        print("Samsung S20E")
    elif idProduto == 2:
        print("Samsung A34")
    elif idProduto == 3:
        print("moto g84")
    elif idProduto == 4:
        print("Smart TV 43 LG")
    else:
        print("PlayStation5")


conexao.commit()
conexao.close ()