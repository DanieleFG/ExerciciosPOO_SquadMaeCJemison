from .obra import Obra


class Manga(Obra):
    def tipo_obra(self) -> str:
        return "Manga"
