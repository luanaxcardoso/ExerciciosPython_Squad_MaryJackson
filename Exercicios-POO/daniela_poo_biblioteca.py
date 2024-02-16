# RESOLUÇÃO DESAFIO POO: GERENCIAMENTO DE BIBLIOTECA

from abc import abstractmethod #import para tornar a classe abstrata 

import sqlite3 # import para usar o dbeaver
conexao = sqlite3.connect('banco-poo-db')  # nome do arquivo criado no Dbeaver
cursor = conexao.cursor()

class Livro:
    lista_genero = [] #lista global para armazenar os generos
    livros_disponiveis = [] # lista global para armazenar os livros disponiveis

    def __init__(self, autor, titulo, editora, genero, emprestado):
        self.autor = autor 
        self.titulo = titulo
        self.editora = editora
        self.genero = genero
        self.emprestado = emprestado
        self.livro() # chama o método livro para imprimir as informações
    
    def livro(self):
        print(f'Livro: {self.titulo}, autor: {self.autor}, editora: {self.editora}, gênero: {self.genero}, emprestado: {self.emprestado}')
        
        Livro.lista_genero.append(self.genero) # adiciona o gênero à lista 'lista_genero'
        
        if self.emprestado == 0 :  # se emprestado == false (significa que o livro está disponivel)
            Livro.livros_disponiveis.append(self)  # armazena na lista 'livros_disponiveis'
        
    @staticmethod  # método estático, para listar os generos
    def generos():
        print('Gêneros cadastrados: ')
        for item in Livro.lista_genero:   # laço de repetição para listar o vetor
            print(f' - {item}')
    
    @staticmethod  # método estático, para listar os livros disponiveis
    def disponiveis():
        print('Livros disponíveis: ') 
        for livro in Livro.livros_disponiveis: # laço de repetição para listar o vetor
            print(f' - Título: {livro.titulo}, autor: {livro.autor}')  # listando os atributos desejáveis do livro
        
    @abstractmethod  #método abstrato dentro de classe abstrata
    def emprestar(self):
        emprestado = emprestado #deve ser instaciado na classe filha 

class Usuario:
    def __init__(self, nome, telefone, nacionalidade):
        self.nome = nome
        self.telefone = telefone
        self.nacionalidade = nacionalidade

class Emprestar(Livro): # herança da classe Livro
    def __init__(self, autor, titulo, editora, genero, emprestado):
        super().__init__(autor, titulo, editora, genero, emprestado)  #método super() para chamar a herança

        self.emprestado(True) # instancia o atributo emprestado como true
        print(f'Livro "{self.titulo}" emprestado.')

'''
############## COMANDOS POO ##############
# Instanciando e listando livros:
print('Livros cadastrados:')
dado = Livro("Itamar Vieira Junior","Torto arado","Arqueiro","Realismo Mágico",False)
dado = Livro("Ana Paula Maia","Enterre seus mortos","Saraiva","Drama",True)
dado = Livro("Margaret Atwood","O conto da aia","Rocco","Distopia",True)
dado = Livro("Stephen King", "It", "Viking Press", "Terror", False)
dado = Livro("George Orwell", "1984", "Penguin Books", "Ficção Científica", False)
dado = Livro("Agatha Christie", "O Assassinato no Expresso Oriente", "Globo Livros", "Mistério", True)
dado = Livro("J.R.R. Tolkien", "O Senhor dos Anéis: A Sociedade do Anel", "Martins Fontes", "Fantasia", False)
dado = Livro("Clarice Lispector", "A Hora da Estrela", "Rocco", "Literatura Brasileira", True)
print('')

# Listando os generos:
dado.generos()
print('')

#listando os livros disponiveis
dado.disponiveis()
'''

conexao.commit() 
conexao.close()
