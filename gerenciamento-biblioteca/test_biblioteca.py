import unittest
from pessoa import Usuario, Autor
from livro import Livro
from biblioteca import Biblioteca

class TestBiblioteca(unittest.TestCase):
    def setUp(self):
        self.biblioteca = Biblioteca()

        # Criando usuários
        self.usuario1 = Usuario(id_usuario=1, nome="João", telefone="123456789", nacionalidade="Brasileiro")
        self.usuario2 = Usuario(id_usuario=2, nome="Maria", telefone="987654321", nacionalidade="Português")
        self.usuario3 = Usuario(id_usuario=3, nome="Carlos", telefone="111111111", nacionalidade="Espanhol")
        self.usuario4 = Usuario(id_usuario=4, nome="Pedro", telefone="222222222", nacionalidade="Francês")

        # Criando autores
        self.autor1 = Autor('Machado de Assis')
        self.autor2 = Autor('José de Alencar')
        self.autor3 = Autor('Clarice Lispector')
        self.autor4 = Autor('Carlos Drummond de Andrade')

        # Criando livros
        self.livro1 = Livro('Dom Casmurro', 'Editora A', [self.autor1], 'Romance', 2, 1) # Objeto com limite de empréstimo
        self.livro2 = Livro('Senhora', 'Editora B', [self.autor2], 'Romance', 0)
        self.livro3 = Livro('A hora da estrela', 'Editora C', [self.autor3], 'Romance', 7)
        self.livro4 = Livro('A rosa do povo', 'Editora D', [self.autor4], 'Poesia', 5)
        self.livro5 = Livro('Memórias póstumas de Brás Cubas', 'Editora E', [self.autor1], 'Romance', 9)

        # Adicionando usuários e livros à biblioteca
        self.biblioteca.adicionar_usuario(self.usuario1)
        self.biblioteca.adicionar_usuario(self.usuario2)
        self.biblioteca.adicionar_usuario(self.usuario3)
        self.biblioteca.adicionar_livro(self.livro1)
        self.biblioteca.adicionar_livro(self.livro2)
        self.biblioteca.adicionar_livro(self.livro3)
        self.biblioteca.adicionar_livro(self.livro4)

    def test_emprestar_livro(self):
        self.biblioteca.emprestar_livro(self.usuario1, self.livro1)
        self.assertEqual(len(self.biblioteca.registros), 1)
        self.assertEqual(self.livro1.exemplares_disponiveis, 1)

    def test_limite_emprestimo(self):
        self.biblioteca.emprestar_livro(self.usuario1, self.livro1)
        with self.assertRaises(ValueError):
            self.biblioteca.emprestar_livro(self.usuario1, self.livro1)

    def test_usuario_nao_cadastrado(self):
        with self.assertRaises(ValueError):
            self.biblioteca.emprestar_livro(self.usuario4, self.livro1)

    def test_livro_sem_exemplares_disponiveis(self):
        with self.assertRaises(ValueError):
            self.biblioteca.emprestar_livro(self.usuario3, self.livro2)

    def test_devolver_livro(self):
        self.biblioteca.emprestar_livro(self.usuario1, self.livro1)
        self.biblioteca.devolver_livro(self.usuario1, self.livro1)
        self.assertEqual(self.livro1.exemplares_disponiveis, 2)

    def test_usuario_atingiu_limite_emprestimos(self):
        self.biblioteca.emprestar_livro(self.usuario1, self.livro1)
        self.biblioteca.devolver_livro(self.usuario1, self.livro1)
        with self.assertRaises(ValueError):
            self.biblioteca.emprestar_livro(self.usuario1, self.livro1)

if __name__ == '__main__':
    unittest.main()
