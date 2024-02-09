from datetime import datetime
from typing import Optional

from .obra import Obra
from .pessoa import Pessoa


class Emprestimo:
    def __init__(self, obra: Obra, usuario: Pessoa, exemplar: int, data_emprestimo: datetime, data_devolucao: Optional[datetime] = None, estado: str = "emprestado"):
        self.obra = obra
        self.usuario = usuario
        self.exemplar = exemplar
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.estado = estado

    def devolver(self, data_devolucao: Optional[datetime] = None) -> None:
        self.data_devolucao = data_devolucao if data_devolucao else datetime.now()
        self.estado = "devolvido"
