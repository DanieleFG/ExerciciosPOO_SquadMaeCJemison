from abc import ABC, abstractmethod
from typing import List


class Obra(ABC):
    def __init__(self, titulo: str, editora: str, generos: List[str]):
        self.titulo = titulo
        self.editora = editora
        self.generos = generos

    @abstractmethod
    def tipo_obra(self) -> str:
        pass
