import sqlite3
from datetime import datetime

conexao = sqlite3.connect('bd_library')
cursor = conexao.cursor()


#Cria a tabelas
# cursor.execute(
#   '''CREATE TABLE livros(
#     id INTEGER PRIMARY KEY AUTOINCREMENT, 
#     titulo VARCHAR(80), 
#     genero TEXT CHECK(genero IN ('comedia', 'romance', 'ficcao', 'autoajuda', 'pesquisa', 'suspense')),
#     renovacao_maxima INT
#   );'''
# )

# cursor.execute(
#   '''CREATE TABLE autores(
#     id INTEGER PRIMARY KEY AUTOINCREMENT, 
#     nome VARCHAR(20), 
#     sobrenome VARCHAR(50)
#   );'''
# )

# cursor.execute(
#   '''CREATE TABLE livro_autor(
#     livro_id INTEGER, 
#     autor_id INTEGER, 
#     FOREIGN KEY (livro_id) REFERENCES livros(id), 
#     FOREIGN KEY (autor_id) REFERENCES autores(id)
#   );'''
# )

# cursor.execute(
#   '''CREATE TABLE usuarios(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome VARCHAR(20),
#     nacionalidade TEXT CHECK(nacionalidade IN ('nac. brasileira', 'nac. extrangeira')),
#     telefone VARCHAR(15)  
#   );'''
# )

# cursor.execute(
#   '''CREATE TABLE emprestimos(
#     dt_emprestimos,
#     dt_devolucao,
#     estado_emprestimo TEXT CHECK(estado_emprestimo IN ('emprestado','devolvido')),
#     livro_id INTEGER,
#     usuario_id INTEGER,
#     FOREIGN KEY (livro_id) REFERENCES livros(id), 
#     FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
#   );'''
# )

#Excluir tabela criada errado
#cursor.execute('DROP TABLE biblioteca')

#Popular Tabelas e consultar dados

### Tabela Usuários
# cursor.execute('''INSERT INTO usuarios(id, nome, nacionalidade, telefone) VALUES (NULL, 'Ana Paula', 'nac. brasileira', '11 93456-6745')''')
# cursor.execute('INSERT INTO usuarios(id, nome, nacionalidade, telefone) VALUES (NULL, "Peter Korl", "nac. extrangeira", "345 56783456")')
# cursor.execute('''INSERT INTO usuarios(id, nome, nacionalidade, telefone) VALUES(NULL, 'Bento Sousa', 'nac. brasileira', '15 93456-4532')''')
# cursor.execute('''INSERT INTO usuarios(id, nome, nacionalidade, telefone) VALUES(NULL, 'Carla Costa', 'nac. brasileira', '12 93646-6090')''')

# users = cursor.execute("SELECT * FROM usuarios")
# print('\nLista de usuários:\n')
# for user in users:
#   print(user)
# print('\n------------------------------###------------------------------\n')

### Tabela Livros

livros = [
  ('A Divina Comedia', 'comedia', 5),
  ('O Hobbit', 'ficcao', None),
  ('Fundamentos da Metodologia Cientifica', 'pesquisa', 20),
  ('Holly', 'suspense', None)
]

#cursor.executemany('''INSERT INTO livros (id, titulo, genero, renovacao_maxima) VALUES (NULL, ?, ?, ?)''', livros)

# books = cursor.execute("SELECT * FROM livros")
# print('\nLista de livros:\n')
# for book in books:
#   print(book)
# print('\n------------------------------###------------------------------\n')


### Tabela autores
autores = [
  ('Dante', 'Alighieri'),
  ('Stephen', 'King'),
  ('J.R.R', 'Tolkien'),
  ('Mariana', 'Marconi'),
  ('Eva', 'Lakatos'),
]

# cursor.executemany('''INSERT INTO autores (id, nome, sobrenome) VALUES (NULL, ?, ?)''', autores)

# authors = cursor.execute("SELECT * FROM autores")
# print('\nLista de autores:\n')
# for auth in authors:
#   print(auth)
# print('\n------------------------------###------------------------------\n')

#Deleta dados inserido 2x
#cursor.execute('DELETE FROM autores where id=6')

### Tabela autores_livros
autor_livro = [
  (1, 1),
  (2, 3),
  (3, 4),
  (3, 5),
  (4, 2),
]

#cursor.executemany('''INSERT INTO livro_autor (livro_id, autor_id) VALUES (?, ?)''', autor_livro)

# auth_book = cursor.execute("SELECT * FROM livro_autor")
# print('\nLista de relacao Livros/Autores:\n')
# for ab in auth_book:
#   print(ab)
# print('\n------------------------------###------------------------------\n')


### Tabela emprestimos

# alterando o tipo de uma coluna
#cursor.execute('ALTER TABLE emprestimos DROP COLUMN dt_emprestimos')
#cursor.execute('ALTER TABLE emprestimos ADD COLUMN dt_emprestimos DATE')
#cursor.execute('ALTER TABLE emprestimos DROP COLUMN dt_devolucao')
#cursor.execute('ALTER TABLE emprestimos ADD COLUMN dt_devolucao DATE')

emprestimos = [
  ('2024-01-15', '2024-02-10', 'emprestado', 2, 4),
  ('2024-02-10', '2024-03-10', 'emprestado', 4, 3),
  ('2024-01-05', '2024-02-05', 'devolvido', 1, 1)
  
]

#cursor.executemany('''INSERT INTO emprestimos (dt_emprestimos, dt_devolucao, estado_emprestimo, livro_id, usuario_id) VALUES (?, ?, ?, ?, ?)''', emprestimos)

hoje = datetime.now()
emprestimos_atraso = cursor.execute(
    '''SELECT * FROM emprestimos WHERE 
    dt_devolucao < ? AND estado_emprestimo="emprestado"''', (hoje,))
print("\nEmpréstimos em atraso:\n")
for atrasados in emprestimos_atraso:
    print(atrasados)
print('\n------------------------------###------------------------------\n')

emprestados = cursor.execute(
    '''SELECT * FROM emprestimos WHERE estado_emprestimo="emprestado"''')
print("\nLivros emprestados:\n")
for emprestado in emprestados:
    print(emprestado)
print('\n------------------------------###------------------------------\n')

disponiveis = cursor.execute(
    '''SELECT * FROM emprestimos WHERE estado_emprestimo="devolvido"''')
print("\nLivros disponíveis:\n")
for disponivel in disponiveis:
    print(disponivel)
print('\n------------------------------###------------------------------\n')

# Salvar as alterações e fechar a conexão
conexao.commit()
conexao.close()