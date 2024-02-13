from pessoa import Usuario, Autor
from livro import Livro
from biblioteca import Biblioteca

## criando objetos usuario
usuario1 = Usuario(id_usuario=1, nome="João", telefone="123456789",nacionalidade="Brasileiro")
usuario2 = Usuario(id_usuario=2, nome="Maria", telefone="987654321", nacionalidade="Português")
usuario3 = Usuario(id_usuario=3, nome="Carlos", telefone="111111111", nacionalidade="Espanhol")
# objeto criado mas não adicionado a biblioteca
usuario4 = Usuario(id_usuario=4, nome="Pedro", telefone="222222222", nacionalidade="Francês")

## criando objetos autor
autor1 = Autor('Machado de Assis')
autor2 = Autor('José de Alencar')
autor3 = Autor('Clarice Lispector')
autor4 = Autor('Carlos Drummond de Andrade')

## criando objetos livro
livro1 = Livro('Dom Casmurro', 'Editora A', [autor1], 'Romance', 2, 2) # Objeto com limite de empréstimo
livro2 = Livro('Senhora', 'Editora B', [autor2], 'Romance', 1)
livro3 = Livro('A hora da estrela', 'Editora C', [autor3], 'Romance', 7)
livro4 = Livro('A rosa do povo', 'Editora D', [autor4], 'Poesia', 5)

# Objeto criado mas não adicionado a biblioteca
livro5 = Livro('Memórias póstumas de Brás Cubas', 'Editora E', [autor1], 'Romance', 9)

## Criando objeto biblioteca
biblioteca = Biblioteca()

## Adicionando usuario a biblioteca
biblioteca.adicionar_usuario(usuario1)
biblioteca.adicionar_usuario(usuario2)
biblioteca.adicionar_usuario(usuario3)

## Adicionando livros a biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)
biblioteca.adicionar_livro(livro4)
 
#livro não cadastrado
try:
    biblioteca.emprestar_livro(usuario1, livro5)
except ValueError as error:
    print(error)

#usuario não cadastrado
try:
    biblioteca.emprestar_livro(usuario4, livro1)
except ValueError as error:
    print(error)

#livro sem exemplares disponíveis
try: 
    biblioteca.emprestar_livro(usuario3, livro1)
except ValueError as error:
    print(error)

# devolvendo livro
biblioteca.emprestar_livro(usuario1, livro1)
biblioteca.devolver_livro(usuario1, livro1)
biblioteca.emprestar_livro(usuario1, livro1)
biblioteca.devolver_livro(usuario1, livro1)


#usuario atingiu o limite de empréstimos
try:
    print("Emprestimo de livro 1")
    biblioteca.emprestar_livro(usuario1, livro1)
    biblioteca.devolver_livro(usuario1, livro1)
    biblioteca.emprestar_livro(usuario1, livro1)
    print("Emprestimo com sucesso")
except ValueError as error:
    print(error)

#imprimindo registros
biblioteca.imprimir_registros()

#imprimindo dados da biblioteca
print(biblioteca)
