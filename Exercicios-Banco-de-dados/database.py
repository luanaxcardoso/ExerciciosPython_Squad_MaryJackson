import sqlite3
from datetime import datetime

def conectar_banco_dados(database):
    conn = sqlite3.connect(database)
    return conn

def criar_tabelas(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS autores (
                        id INTEGER PRIMARY KEY,
                        nome TEXT,
                        nacionalidade TEXT
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS livros (
                        id INTEGER PRIMARY KEY,
                        titulo TEXT,
                        editora TEXT,
                        genero TEXT,
                        exemplares_disponiveis INTEGER,
                        autor_id INTEGER,
                        FOREIGN KEY (autor_id) REFERENCES autores(id)
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS emprestimos (
                        id INTEGER PRIMARY KEY,
                        livro_id INTEGER,
                        data_emprestimo TIMESTAMP,
                        data_devolucao TIMESTAMP,
                        estado TEXT,
                        FOREIGN KEY (livro_id) REFERENCES livros(id)
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY,
                        nome TEXT,
                        telefone TEXT,
                        nacionalidade TEXT
                    )''')

    cursor.execute('''INSERT INTO autores (nome, nacionalidade) VALUES
                    ('Paulo Coelho', 'Brasil'),
                    ('Edgar Allan Poe', 'Estados Unidos'),
                    ('H.P. Lovecraft', 'Estados Unidos'),
                    ('Sylvia Plath', 'Estados Unidos'),
                    ('Gillian Flynn', 'Estados Unidos')''')

    cursor.execute('''INSERT INTO usuarios (nome, telefone, nacionalidade) VALUES
                    ('Marcelo', '12934567890', 'Brasil'),
                    ('Maria', '12987-6543210', 'Brasil'),
                    ('Daniel', '1298587456', 'Brasil')''')

    conn.commit()


def fechar_conexao(conn):
    conn.close()

conn = conectar_banco_dados('database.db')

criar_tabelas(conn)


cursor = conn.cursor()

# Inserção de empréstimos
emprestimos = [(1, datetime.now(), 'emprestado'), (2, datetime.now(), 'emprestado')]
cursor.executemany('''INSERT INTO emprestimos (livro_id, data_emprestimo, estado) VALUES (?, ?, ?)''', emprestimos)

# Inserção de livros
livros = [
    ('O Alquimista', 'Rocco', 'Ficção', 10, 1),
    ('O Corvo', 'Editora X', 'Poesia', 5, 2),
    ('Nas Montanhas da Loucura', 'Editora Y', 'Terror', 8, 3),
    ('A Redoma de Vidro', 'Editora Z', 'Romance', 7, 4),
    ('Garota Exemplar', 'Editora W', 'Suspense', 12, 5)
]
cursor.executemany('''INSERT INTO livros (titulo, editora, genero, exemplares_disponiveis, autor_id) VALUES (?, ?, ?, ?, ?)''', livros)

conn.commit()

# Exemplo de consulta de livros disponíveis
cursor.execute('''SELECT * FROM livros WHERE exemplares_disponiveis > 0''')
livros_disponiveis = cursor.fetchall()
print("Livros Disponíveis:")
for livro in livros_disponiveis:
    print(livro)
print()

# Exemplo de consulta de livros emprestados
cursor.execute('''SELECT * FROM emprestimos WHERE estado = 'emprestado' ''')
livros_emprestados = cursor.fetchall()
print("Livros Emprestados:")
for livro in livros_emprestados:
    print(livro)
print()

# Exemplo de consulta de livros por autor
autor = 'Paulo Coelho'
cursor.execute('''SELECT * FROM livros INNER JOIN autores ON livros.autor_id = autores.id WHERE autores.nome = ?''', (autor,))
livros_autor = cursor.fetchall()
print(f"Livros escritos por {autor}:")
for livro in livros_autor:
    print(livro)
print()

# Exemplo de consulta de exemplares disponíveis de um livro específico
livro_id = 1
cursor.execute('''SELECT exemplares_disponiveis FROM livros WHERE id = ?''', (livro_id,))
exemplares_disponiveis = cursor.fetchone()
if exemplares_disponiveis:
    print(f"Número de exemplares disponíveis do livro com ID {livro_id}: {exemplares_disponiveis[0]}")
else:
    print(f"Não há informações sobre o livro com ID {livro_id}")
print()

# Exemplo de consulta de empréstimos em atraso
hoje = datetime.now()
cursor.execute('''SELECT * FROM emprestimos WHERE data_devolucao < ?''', (hoje,))
emprestimos_atraso = cursor.fetchall()
print("Empréstimos em atraso:")
for emprestimo in emprestimos_atraso:
    print(emprestimo)

fechar_conexao(conn)
