from typing import List
from abc import ABC, abstractmethod


class Obra(ABC):
    def __init__(self, titulo: str, editora: str, generos: List[str]):
        self.titulo = titulo
        self.editora = editora
        self.generos = generos

    @abstractmethod
    def tipo_obra(self) -> str:
        pass
