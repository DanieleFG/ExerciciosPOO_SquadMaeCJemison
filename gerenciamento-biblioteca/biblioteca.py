from datetime import datetime
from pessoa import Usuario
from livro import Livro

class Emprestimo:
    def __init__(self, usuario: Usuario, livro: Livro, data_emprestimo: datetime):
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = data_emprestimo

    def __str__(self) -> str:
        return f'Usuário: {self.usuario.nome}, Livro: {self.livro.titulo}, Data do empréstimo: {self.data_emprestimo}'

class Biblioteca:
    def __init__(self):
        self._usuarios = []           # Lista de usuários cadastrados na biblioteca
        self._livros = []             # Lista de livros cadastrados na biblioteca
        self.registros = []           # Registro de livros emprestados

    def adicionar_usuario(self, usuario: Usuario):
        if usuario in self._usuarios:
            raise ValueError(f'Usuário {usuario.nome} já cadastrado na biblioteca')
        self._usuarios.append(usuario)

    def adicionar_livro(self, livro: Livro):
        if livro in self._livros:
            raise ValueError(f'Livro {livro.titulo} já cadastrado na biblioteca')
        self._livros.append(livro)

    def emprestar_livro(self, usuario: Usuario, livro: Livro):
        if usuario not in self._usuarios:
            raise ValueError(f'Usuário {usuario.nome} não cadastrado na biblioteca')
        if livro not in self._livros:
            raise ValueError(f'Livro {livro.titulo} não cadastrado na biblioteca')
        if livro.limite_emprestimo is not None:
            # Contar quantos empréstimos o usuário já fez do livro
            emprestimos_usuario = sum(1 for registro in self.registros if registro.usuario == usuario and registro.livro == livro)
            if emprestimos_usuario >= livro.limite_emprestimo:
                raise ValueError(f'Usuário {usuario.nome} já atingiu o limite de empréstimos do livro {livro.titulo}')
        if livro.exemplares_disponiveis == 0:
            raise ValueError(f'Não há exemplares disponíveis do livro {livro.titulo}')
        emprestimo = Emprestimo(usuario, livro, datetime.now())
        self.registros.append(emprestimo)
        livro.exemplares_disponiveis -= 1


    def devolver_livro(self, usuario: Usuario, livro: Livro):
        for emprestimo in self.registros:
            if emprestimo.usuario == usuario and emprestimo.livro == livro:
               # self.registros.remove(emprestimo)
                livro.exemplares_disponiveis += 1
                return
        raise ValueError(f'Livro {livro.titulo} não foi emprestado para o usuário {usuario.nome}')
    
    def imprimir_registros(self):
        registros = '\n'.join([str(registro) for registro in self.registros])
        print(f'\nRegistros de empréstimos\n{registros}')

    def __str__(self) -> str:
        usuarios = '\n'.join([str(usuario) for usuario in self._usuarios])
        livros = '\n'.join([str(livro) for livro in self._livros])
        return f'\nUsuários\n{usuarios}\n\nLivros\n{livros}'
