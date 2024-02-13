from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        return self.__nome
       
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @abstractmethod
    def __str__(self):
        pass

class Autor(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)

    def __str__(self):
        return f'{self.nome}'

class Usuario(Pessoa):
    def __init__(self,id_usuario, nome, telefone, nacionalidade):
        super().__init__(nome)
        self.id_usuario = id_usuario
        self.__telefone = telefone
        self.nacionalidade = nacionalidade

    @property
    def telefone(self):
        return self.__telefone
     
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    def __str__(self):
        return f'Usuário id: {self.id_usuario}, nome {self.nome}, telefone {self.telefone}, nacionalidade {self.nacionalidade}'
