from .obra import Obra


class Revista(Obra):
    def tipo_obra(self) -> str:
        return "Revista"
