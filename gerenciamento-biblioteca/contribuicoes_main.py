from pessoa import Usuario, Autor
from livro import Livro
from biblioteca import Biblioteca

## criando objetos usuario
usuario1 = Usuario(id_usuario=1, nome="João", telefone="123456789",nacionalidade="Brasileiro")
usuario2 = Usuario(id_usuario=2, nome="Maria", telefone="987654321", nacionalidade="Portuguesa")
usuario3 = Usuario(id_usuario=3, nome="Carlos", telefone="111111111", nacionalidade="Espanhol")
usuario4 = Usuario(id_usuario=4, nome="Donato", telefone="876450098", nacionalidade="Brasileiro")
# objeto criado mas não adicionado a biblioteca
usuario5 = Usuario(id_usuario=5, nome="Pedro", telefone="222222222", nacionalidade="Francês")
usuario6 = Usuario(id_usuario=6, nome="Brian", telefone="333333333", nacionalidade="Inglês")

## criando objetos autor
autor1 = Autor('Machado de Assis')
autor2 = Autor('José de Alencar')
autor3 = Autor('Clarice Lispector')
autor4 = Autor('Carlos Drummond de Andrade')
autor5 = Autor('J.D. Salinger')
autor6 = Autor('Franz Kafka')

## criando objetos livro
livro1 = Livro('Dom Casmurro', 'Editora A', [autor1], 'Romance', 2, 2) # Objeto com limite de empréstimo
livro2 = Livro('Senhora', 'Editora B', [autor2], 'Romance', 1, 1) # Objeto com limite de empréstimo
livro3 = Livro('A hora da estrela', 'Editora C', [autor3], 'Romance', 7)
livro4 = Livro('A rosa do povo', 'Editora D', [autor4], 'Poesia', 5)
livro5 = Livro('O Apanhador no Campo de Centeio', 'Editora do Autor', [autor5], 'Romance', 3)
livro6 = Livro('A Metamorfose', 'Editora Companhia das Letras', [autor6], 'Ficção', 3)
# Objeto criado mas não adicionado a biblioteca
livro7 = Livro('Memórias póstumas de Brás Cubas', 'Editora E', [autor1], 'Romance', 9)

## Criando objeto biblioteca
biblioteca = Biblioteca()

## Adicionando usuario a biblioteca
biblioteca.adicionar_usuario(usuario1)
biblioteca.adicionar_usuario(usuario2)
biblioteca.adicionar_usuario(usuario3)
biblioteca.adicionar_usuario(usuario4)

## Adicionando livros a biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)
biblioteca.adicionar_livro(livro4)
biblioteca.adicionar_livro(livro5)
biblioteca.adicionar_livro(livro6)
 
#livro não cadastrado
try:
    biblioteca.emprestar_livro(usuario1, livro7)
except ValueError as error:
    print(error)

#usuarios não cadastrados
try:
    biblioteca.emprestar_livro(usuario5, livro1)
except ValueError as error:
    print(error)
    
try:
    biblioteca.emprestar_livro(usuario6, livro7)
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
biblioteca.emprestar_livro(usuario4, livro5)
biblioteca.devolver_livro(usuario4, livro5)

#usuario atingiu o limite de empréstimos
try:
    print("Emprestimo de livro 1")
    biblioteca.emprestar_livro(usuario2, livro1)
    biblioteca.emprestar_livro(usuario1, livro1)
    print("Emprestimo com sucesso")
except ValueError as error:
    print(error)

#imprimindo registros
biblioteca.imprimir_registros()

#imprimindo dados da biblioteca
print(biblioteca)
