from datetime import datetime
import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS livros (id INT PRIMARY KEY, titulo TEXT, editora TEXT, genero TEXT, quantidade_exemplares INT, autor_id INT, FOREIGN KEY (autor_id) REFERENCES autores (id) )')
cursor.execute('CREATE TABLE IF NOT EXISTS autores (id INT PRIMARY KEY, nome TEXT, nacionalidade TEXT)')
cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (id INT PRIMARY KEY, nome TEXT, telefone TEXT, nacionalidade TEXT)')
cursor.execute('CREATE TABLE IF NOT EXISTS emprestimos (id INT PRIMARY KEY, livro_id INT, data_emprestimo TIMESTAMP, data_devolucao TIMESTAMP, status TEXT, FOREIGN KEY (livro_id) REFERENCES livros (id))')
cursor.execute('INSERT INTO autores(nome, nacionalidade) VALUES ("David Nicholls", "Britânica"), ("Jojo Moyes", "Britânica"), ("Igor Pires", "Brasileira"), ("Itamar Vieira Junior", "Brasileira"), ("Michel Foucault", "Francesa")')
cursor.execute('INSERT INTO usuarios (nome, telefone, nacionalidade) VALUES ("Pedro", 7981234567, "Brasileira"), ("Liandra", 7981224567, "Brasileira"), ("Giovanna", 7981234587, "Brasileira"), ("Leticia", 7981234569, "Brasileira"), ("Sergio", 7981734567, "Brasileira")')
cursor.execute('INSERT INTO livros (titulo, editora, genero, quantidade_exemplares, autor_id) VALUES ("One Day", "Intrínseca", "Romance", 8, 1)')
cursor.execute('INSERT INTO livros (titulo, editora, genero, quantidade_exemplares, autor_id) VALUES ("A última carta de amor", "Intrínseca", "Romance", 12, 2)')
cursor.execute('INSERT INTO livros (titulo, editora, genero, quantidade_exemplares, autor_id) VALUES ("Texto cruéis demais para serem lidos rapidamente", "Globo Alt", "Romance", 7, 3)')
cursor.execute('INSERT INTO livros (titulo, editora, genero, quantidade_exemplares, autor_id) VALUES ("Torto Arado", "Todavia", "Romance", 5, 4)')
cursor.execute('INSERT INTO livros (titulo, editora, genero, quantidade_exemplares, autor_id) VALUES ("Vigiar e Punir", "Editora Vozes", "Romance", 13, 5)')


conexao.commit() #o envio só acontece aqui
conexao.close #para evitar conflitos, encerra o processo