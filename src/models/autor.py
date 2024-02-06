from .pessoa import Pessoa


class Autor(Pessoa):
    def __init__(self, nome: str, telefone: str, nacionalidade: str):
        super().__init__(nome, telefone, nacionalidade)