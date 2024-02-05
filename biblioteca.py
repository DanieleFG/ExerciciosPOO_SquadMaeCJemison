class Biblioteca():
    def __init__(self, nome, telefone, nacionalidade):
        self.nome = nome
        self.telefone = telefone
        self.nacionalidade = nacionalidade
        self.data_emprestimo = ''
        self.data_devolucao = ''
        self.estado = ''

   
        
class Livro():
    def __init__(self, titulo, editora, autores):
        self.titulo = titulo
        self.editora = editora
        self.autores= [autores]
        self.lista_de_generos = []
        self.lista_de_exemplares = []


usuario1 = Biblioteca('Dany','9999 9999', 'brazileira')
livroRomance = Livro('Poliana','Editora Lafonte', ['Eleonor'])


print(usuario1.nome)
print(livroRomance.autores)


