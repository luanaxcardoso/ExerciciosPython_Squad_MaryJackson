from datetime import datetime, timedelta
from abc import ABC, abstractmethod
from database import conectar_banco_dados, fechar_conexao
#rodar com arquivo database.py

class EntidadeBiblioteca(ABC):
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

    @abstractmethod
    def obter_detalhes(self):
        pass

class Autor(EntidadeBiblioteca):
    def obter_detalhes(self):
        return f'Autor: {self.nome}, Telefone: {self.telefone}, Nacionalidade: {self.nacionalidade}'

class Livro(EntidadeBiblioteca):
    def __init__(self, titulo, editora, generos, exemplares_disponiveis, max_renovacoes=None):
        super().__init__(titulo, editora, generos)
        self._exemplares_disponiveis = exemplares_disponiveis
        self._max_renovacoes = max_renovacoes
        self.editora = editora
        self.generos = generos

    @property
    def exemplares_disponiveis(self):
        return self._exemplares_disponiveis

    def emprestar_exemplar(self):
        if self._exemplares_disponiveis > 0:
            self._exemplares_disponiveis -= 1
            return True
        else:
            return False

    def devolver_exemplar(self):
        self._exemplares_disponiveis += 1

    def obter_detalhes(self):
        return f'Livro: {self.nome}, Editora: {self.editora}, Gêneros: {self.generos}' 

class Usuario(EntidadeBiblioteca):
    def obter_detalhes(self):
        return f'Usuário: {self.nome}, Telefone: {self.telefone}, Nacionalidade: {self.nacionalidade}'

class Emprestimo:
    def __init__(self, livro, usuario):
        self._livro = livro
        self._usuario = usuario
        self._data_emprestimo = datetime.now()
        self._data_devolucao = self._data_emprestimo + timedelta(days=7)  # Data de devolução é a data de empréstimo + 7 dias
        self._estado = "emprestado"
        self._num_renovacoes = 0

    def devolver(self):
        self._data_devolucao = datetime.now()
        self._estado = "devolvido"

class Biblioteca:
    def __init__(self):
        self._livros = []
        self._usuarios = []
        self._emprestimos = []
        self.conn = conectar_banco_dados('database.db')

    def fechar_conexao(self):
        fechar_conexao(self.conn)

    def adicionar_livro(self, livro):
        self._livros.append(livro)

    def adicionar_usuario(self, usuario):
        self._usuarios.append(usuario)
        
    def adicionar_usuario_bd(self, usuario):
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO usuarios (nome, telefone, nacionalidade) VALUES (?, ?, ?)''', (usuario.nome, usuario.telefone, usuario.nacionalidade))
        self.conn.commit()
        cursor.close()

    def adicionar_usuarios_iniciais(self):
        usuarios_iniciais = [
            Usuario("Luana", "129583456", "Brasil"),
            Usuario("Bruno", "1298654321", "Brasil"),
            Usuario("Marta", "129123456", "Brasil"),
        ]
        for usuario in usuarios_iniciais:
            self.adicionar_usuario_bd(usuario)

    def realizar_emprestimo(self, livro, usuario):
        if livro.emprestar_exemplar():
            emprestimo = Emprestimo(livro, usuario)
            self._emprestimos.append(emprestimo)
            return True
        else:
            return False

    def renovar_emprestimo(self, emprestimo):
        if emprestimo in self._emprestimos:
            if emprestimo._livro._max_renovacoes is None or emprestimo._num_renovacoes < emprestimo._livro._max_renovacoes:
                emprestimo._data_emprestimo = datetime.now()
                emprestimo._data_devolucao = self._data_emprestimo + timedelta(days=7)  # Data de devolução é a data de empréstimo + 7 dias
                emprestimo._num_renovacoes += 1
                return True
        return False

    def registrar_devolucao(self, emprestimo):
        if emprestimo in self._emprestimos:
            
            emprestimo._data_devolucao = datetime.now()
            emprestimo._estado = "devolvido"
            emprestimo._livro.devolver_exemplar()
            self._emprestimos.remove(emprestimo)
            return True
        return False

    @property
    def livros(self):
        return self._livros

    @property
    def usuarios(self):
        return self._usuarios

    @property
    def emprestimos(self):
        return self._emprestimos

biblioteca = Biblioteca()
biblioteca.adicionar_usuarios_iniciais()
biblioteca.fechar_conexao()
