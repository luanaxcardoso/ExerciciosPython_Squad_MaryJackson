# Classe Autor: Representa um autor de livros
class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade

# Classe Livro: Representa um livro na biblioteca
class Livro:
    def __init__(self, titulo, editora, generos, exemplares_disponiveis, renovacoes_max):
        self.titulo = titulo
        self.editora = editora
        self.generos = generos
        self.exemplares_disponiveis = exemplares_disponiveis
        self.renovacoes_max = renovacoes_max
        self.autores = []

    def adicionar_autor(self, autor):
        # Método para adicionar autor ao livro
        self.autores.append(autor)

# Classe Usuario: Representa um usuário da biblioteca
class Usuario:
    def __init__(self, nome, telefone, nacionalidade):
        self.nome = nome
        self.telefone = telefone
        self.nacionalidade = nacionalidade

# Classe Biblioteca: Representa a biblioteca e suas operações
class Biblioteca:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.usuarios = []
        self.livros = []
        self.emprestimos = []

    def cadastrar_usuario(self, usuario):
        # Método para cadastrar um novo usuário na biblioteca
        self.usuarios.append(usuario)

    def cadastrar_livro(self, livro):
        # Método para cadastrar um novo livro na biblioteca
        self.livros.append(livro)

    def realizar_emprestimo(self, livro, usuario, data_emprestimo, data_devolucao):
        # Método para realizar o empréstimo de um livro para um usuário
        # Aqui você implementaria a lógica, como verificar se o livro está disponível, etc.
        pass

# Exemplo de Uso:
autor1 = Autor("Autor 1", "Nacionalidade 1")
livro1 = Livro("Livro 1", "Editora A", ["Ação", "Aventura"], 5, 2)
livro1.adicionar_autor(autor1)

usuario1 = Usuario("Usuario 1", "123456789", "Brasileira")

biblioteca = Biblioteca("Biblioteca Central", "987654321")
biblioteca.cadastrar_usuario(usuario1)
biblioteca.cadastrar_livro(livro1)
