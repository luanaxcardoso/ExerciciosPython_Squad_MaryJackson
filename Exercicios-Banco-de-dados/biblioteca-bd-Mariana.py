import sqlite3
import datetime

def conectar_banco_dados(database):
    conn = sqlite3.connect(database)
    return conn

#Criação das tabelas no banco de dados
def criar_tabelas(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Autor (
                    id INTEGER PRIMARY KEY,
                    nome TEXT,
                    nacionalidade TEXT
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Livros (
                    id INTEGER PRIMARY KEY,
                    titulo TEXT,
                    editora TEXT,
                    exemplares_disponiveis INTEGER,
                    autor_id INTEGER,
                    FOREIGN KEY (autor_id) REFERENCES autores(id)
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Usuarios (
                    id INTEGER PRIMARY KEY,
                    nome TEXT,
                    telefone TEXT,
                    nacionalidade TEXT
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Emprestimos (
                    id INTEGER PRIMARY KEY,
                    livros_id INTEGER,
                    data_emprestimo TIMESTAMP,
                    data_devolucao TIMESTAMP,
                    estado TEXT,
                    FOREIGN KEY (livros_id) REFERENCES Livros(id)
                    )''')

#Inserir dados nas tabelas

    cursor.execute('''INSERT INTO Autor (nome, nacionalidade) VALUES 
                    ('Gabriel Garcia Marquez', 'Mexicano'),
                    ('Clarice Lispector', 'Brasileira'),
                    ('Nicholas Sparks', 'Americano'),
                    ('Edgar Allan Poe', 'Americano'),
                    ('José Saramago', 'Português'),
                    ('Virginia Woolf', 'Inglesa'),
                    ('Conceição Evaristo', 'Brasileira'),
                    ('Cecília Meireles', 'Brasileira')''')
    
    
    cursor.execute('''INSERT INTO Usuarios (nome, telefone, nacionalidade) VALUES 
                    ('Mariana Mehler', '987654321', 'Brasileira'),
                    ('Ana Pereira', '952152415', 'Portuguesa'),
                    ('Allan Castro', '985652415', 'Brasileiro'),
                    ('Rafael Nogueira', '995862514', 'Brasileiro'),
                    ('Carmen Batistán', '985424154', 'Espanhola'),
                    ('Pedro Rachadel', '95452145', 'Brasileiro'),
                    ('Jim Noyles', '965214256', 'Americano'),
                    ('Enrico Mastieri', '954874514', 'Italiano'),
                    ('Laura Torres', '958474514', 'Brasileira'),
                    ('Felipe Bastos', '95482415', 'Brasileiro'),
                    ('Marina Amarante', '9852415685', 'Brasileira')''')
    
    conn.commit()

def fechar_conexao(conn):
    conn.close()

conn = conectar_banco_dados('database.db')

criar_tabelas(conn)

cursor = conn.cursor()

#Empréstimos
Emprestimos = [(1, datetime.now(), 'emprestado'), (2, datetime.datetime.now(), 'emprestado'), (3, datetime.datetime.now(), 'emprestado'), (8, datetime.datetime.now(), 'emprestado')]
cursor.executemany('''INSERT INTO Emprestimos (livros_id, data_emprestimo, estado) VALUES (?, ?, ?)''', Emprestimos)

# ##Livros
Livros = [
    ('Cem Anos de Solidão', 'Record', 1, 1)
    ('A Hora da Estrela', 'Rocco', 5, 2),
    ('O Desejo', 'Editora Arqueiro', 3, 3),
    ('Histórias extraordinárias', 'Editora Companhia das Letras', 2, 4),
    ('As intermitências da Morte', 'Editora Companhia das Letras', 2, 5),
    ('Mrs. Dalloway', 'Editora Penguin-Companhia', 3, 6),
    ("Olhos D'Agua", 'Editora Pallas', 2, 7),
    ('O Menino Azul', 'Editora Global', 1, 8)
]
cursor.executemany('''INSERT INTO livros (titulo, editora, exemplares_disponiveis, autor_id) VALUES (?, ?, ?, ?, ?)''', Livros)

conn.commit()  

#Livros disponíveis
cursor.execute(''''SELECT * FROM livros WHERE exemplares_disponiveis > 0''')
livros_disponiveis = cursor.fetchall()
print("Livros Disponíveis:")
for livro in livros_disponiveis:
    print(livro)
print()

#Consulta de livros emprestados:
cursor.execute('SELECT * FROM Emprestimos WHERE estado = "emprestado"')
livros_emprestados = cursor.fetchall()
print("Livros Emprestados:")
for livro in livros_emprestados:
    print(livro)
print()

#Localizar os livros escritos por um autor específico
Autor = 'Cecília Meireles'
cursor.execute('SELECT * FROM Livros WHERE id_autor IN (SELECT id FROM Autor WHERE nome = ?)', (autor,))
livros_autor = cursor.fetchall()
print(f"Livros escritos por {autor}:")
for livro in livros_autor:
    print(livro)
print()

# Verificar o número de cópias disponíveis de um determinado livro
livro_id = 5
cursor.execute('''SELECT exemplares_disponiveis FROM livros WHERE id = ?''', (livros_id,))
if exemplares_disponiveis:
    print(f"Número de exemplares disponíveis do livro com ID {livros_id}: {exemplares_disponiveis[0]}")
else:
    print(f"Não há informações sobre o livro com ID {livros_id}")
print()

#Empréstimos em atraso
hoje = datetime.now()
cursor.execute('''SELECT exemplares_disponiveis FROM livros WHERE id = ?''', (livros_id,))
exemplares_disponiveis = cursor.fetchone()
if exemplares_disponiveis:
    print(f"Número de exemplares disponíveis do livro com ID {livros_id}: {exemplares_disponiveis[0]}")
else:
    print(f"Não há informações sobre o livro com ID {livros_id}")
print()

#Consulta empréstimo com atraso
hoje = datetime.now()
cursor.execute('''SELECT * FROM emprestimos WHERE data_devolucao < ?''', (hoje,))
emprestimos_atraso = cursor.fetchall()
print("Empréstimos em atraso:")
for emprestimo in emprestimos_atraso:
    print(emprestimo)

fechar_conexao(conn)