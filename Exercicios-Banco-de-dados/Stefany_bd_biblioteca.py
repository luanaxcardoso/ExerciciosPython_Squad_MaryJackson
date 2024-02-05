import sqlite3

# Conectar ao banco de dados (cria o banco se não existir)
conn = sqlite3.connect('exercicio_banco_dados.db')
cursor = conn.cursor()

# Exercício Gerenciamento de Biblioteca
# 1. Criação das Tabelas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Livros (
        LivroID INTEGER PRIMARY KEY,
        Titulo TEXT,
        Editora TEXT,
        Disponivel INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Autores (
        AutorID INTEGER PRIMARY KEY,
        Nome TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS LivroAutor (
        LivroID INTEGER,
        AutorID INTEGER,
        FOREIGN KEY (LivroID) REFERENCES Livros(LivroID),
        FOREIGN KEY (AutorID) REFERENCES Autores(AutorID)
    )
''')

# 2. Inserção de Dados
cursor.execute("INSERT INTO Livros VALUES (1, 'Livro 1', 'Editora A', 1)")
cursor.execute("INSERT INTO Livros VALUES (2, 'Livro 2', 'Editora B', 1)")

cursor.execute("INSERT INTO Autores VALUES (1, 'Autor 1')")
cursor.execute("INSERT INTO Autores VALUES (2, 'Autor 2')")

cursor.execute("INSERT INTO LivroAutor VALUES (1, 1)")
cursor.execute("INSERT INTO LivroAutor VALUES (2, 2)")

# 3. Consultas SQL
# Listar todos os livros disponíveis
cursor.execute("SELECT * FROM Livros WHERE Disponivel = 1")
print("Livros Disponíveis:")
print(cursor.fetchall())

# Encontrar todos os livros emprestados no momento
cursor.execute("SELECT * FROM Livros WHERE Disponivel = 0")
print("\nLivros Emprestados:")
print(cursor.fetchall())

# Localizar os livros escritos por um autor específico
cursor.execute("SELECT Livros.Titulo FROM Livros JOIN LivroAutor ON Livros.LivroID = LivroAutor.LivroID WHERE LivroAutor.AutorID = 1")
print("\nLivros Escritos pelo Autor 1:")
print(cursor.fetchall())

# Verificar o número de cópias disponíveis de um determinado livro
cursor.execute("SELECT Titulo, COUNT(*) FROM Livros WHERE Disponivel = 1 GROUP BY Titulo")
print("\nNúmero de Cópias Disponíveis:")
print(cursor.fetchall())

# Mostrar os empréstimos em atraso
cursor.execute("SELECT * FROM Emprestimos WHERE DataDevolucao < CURRENT_DATE")
print("\nEmpréstimos em Atraso:")
print(cursor.fetchall())

# 4. Atualizações e Exclusões (exemplo: marcar um livro como devolvido)
cursor.execute("UPDATE Livros SET Disponivel = 1 WHERE LivroID = 1")

# Salvar as alterações e fechar a conexão
conn.commit()
conn.close()
