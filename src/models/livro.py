from typing import List, Optional

from .autor import Autor
from .obra import Obra


class Livro(Obra):
    def __init__(self, titulo: str, editora: str, generos: List[str], autores: List[Autor], num_exemplares: int, num_max_renovacoes: Optional[int] = None):
        super().__init__(titulo, editora, generos)
        self.autores = autores
        self.num_exemplares = num_exemplares
        self.num_max_renovacoes = num_max_renovacoes
        self.exemplares_disponiveis = list(range(1, num_exemplares + 1))

    def tipo_obra(self) -> str:
        return "Livro"
