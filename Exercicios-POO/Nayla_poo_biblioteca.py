import datetime
from abc import ABC

class SistemaBiblioteca(ABC):
     def __init__(self, nome, telefone, nacionalidade):
        self._nome = nome
        self._telefone = telefone
        self._nacionalidade = nacionalidade
        
        @property
        def nome(self):
            return self._nome
        
        @property
        def telefone(self):
            return self._telefone
        
        @property
        def nacionalidade(self):
            return self._nacionalidade
        
class Livro(SistemaBiblioteca):
    def __init__(self, titulo, editora, generos, quantidade_exemplares, max_renovacoes = None):
        super().__init__(titulo, editora, generos)
        self.editora = editora
        self.titulo = titulo
        self.generos = generos
        self.quantidade_exemplares = quantidade_exemplares
        self.max_renovacoes =  max_renovacoes
    
    @property
    def quantidade_exemplares(self):
        return self._quantidade_exemplares
    
    def emprestimo_exemplar(self):
        if self._quantidade_exemplares > 0:
            self._quantidade_exemplares -= 1
            return True
        else:
            return False

    def devolucao_exemplar(self):
        self._quantidade_exemplares += 1
        
    def informacoes(self):
        return f'Livro: {self.nome}, Editora: {self.editora}, Gênero: {self.generos}'
        
class Autor(SistemaBiblioteca):
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade
        
class Usuario(SistemaBiblioteca):
    def informacoes(self):
        return f'Nome:{self.nome}, Telefone:{self.telefone}, Nacionalidade:{self.nacionalidade}'

class Emprestimo:
    def __init__(self, livro, usuario):
        self.livro = livro
        self.usuario = usuario
        self._data_emprestimo = datetime.now
        self._data_devolucao = self._data_emprestimo + datetime.timedelta(dias=5)
        self._status_livro = "emprestado"
        
    def devolucao(self):
        self._data_devolucao = datetime.now()
        self._status_livro = "devolvido"
        
class Biblioteca:
    def __init__(self, nome, telefone, nacionalidade):
        self.nome = nome
        self.telefone = telefone
        self.nacionalidade = nacionalidade
        self.usuarios = []
        self.livros = []
        self.emprestimos = []

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)
        
    def adicionar_livro(self, livro):
        self.livros.append(livro)
        
    def emprestar_livro(self, livro, usuario):
        if livro.emprestimo_exemplar():
            emprestimo = Emprestimo(livro, usuario)
            self._emprestimos.append(emprestimo)
            return True
        return False