from datetime import datetime

from models import Autor, Biblioteca, Livro, Pessoa

if __name__ == "__main__":
    autor1 = Autor("Autor 1", "123456789", "Brasileiro")
    autor2 = Autor("Autor 2", "111111111", "Espanhol")
    livro1 = Livro("Livro 1", "Editora A", ["Ficção", "Aventura"], [autor1], num_exemplares=2, num_max_renovacoes=2)
    livro2 = Livro("Livro 2", "Editora B", ["Romance"], [autor1, autor2], num_exemplares=5, num_max_renovacoes=2)
    usuario1 = Pessoa("Usuário 1", "987654321", "Brasileiro")
    biblioteca = Biblioteca("Biblioteca Municipal")

    emprestimo1 = biblioteca.realizar_emprestimo(livro1, usuario1, datetime.now())
    emprestimo2 = biblioteca.realizar_emprestimo(livro2, usuario1, datetime.now())
    emprestimo3 = biblioteca.realizar_emprestimo(livro2, usuario1, datetime.now())
    emprestimo4 = biblioteca.realizar_emprestimo(livro2, usuario1, datetime.now())
    biblioteca.listar_emprestimos()

    emprestimo1.devolver()

    biblioteca.listar_emprestimos()
