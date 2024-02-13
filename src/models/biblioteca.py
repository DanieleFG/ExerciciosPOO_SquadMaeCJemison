from datetime import datetime
from typing import List, Optional

from .emprestimo import Emprestimo
from .livro import Livro
from .pessoa import Pessoa


class Biblioteca:
    def __init__(self, nome: str):
        self.nome = nome
        self.emprestimos: List[Emprestimo] = []

    def realizar_emprestimo(self, obra: Livro, usuario: Pessoa, data_emprestimo: datetime) -> Optional[Emprestimo]:
        if obra.exemplares_disponiveis:
            exemplar = obra.exemplares_disponiveis.pop(0)
            emprestimo = Emprestimo(obra, usuario, exemplar, data_emprestimo)
            self.emprestimos.append(emprestimo)
            return emprestimo
        else:
            print(f"Não há exemplares disponíveis para empréstimo de '{obra.titulo}'")
            return None

    def listar_emprestimos(self) -> None:
        for emprestimo in self.emprestimos:
            print(f"Obra: {emprestimo.obra.titulo}, Exemplar: {emprestimo.exemplar}, Usuário: {emprestimo.usuario.nome}, Estado: {emprestimo.estado}")
