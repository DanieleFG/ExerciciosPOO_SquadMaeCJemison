from typing import List
from pessoa import Autor

class Livro:
    def __init__(self, titulo: str, editora: str, autor: List['Autor'], genero: str, exemplares_disponiveis: int, limite_emprestimo=None):
        self.titulo = titulo
        self.editora = editora
        self.autor = autor
        self.genero = genero
        self.exemplares_disponiveis = exemplares_disponiveis
        self.limite_emprestimo = limite_emprestimo

    
    def __str__(self):
        autores = ', '.join([str(autor) for autor in self.autor])
        return f'Título: {self.titulo}, Editora: {self.editora}, Autor(es): {autores}, Gênero: {self.genero}, Exemplares disponíveis: {self.exemplares_disponiveis}, Limite de empréstimo: {self.limite_emprestimo}'
