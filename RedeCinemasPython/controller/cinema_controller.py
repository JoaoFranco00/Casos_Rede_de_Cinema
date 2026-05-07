from service.cinema_service import CinemaService


class CinemaController:

    def __init__(self):
        self.service = CinemaService()

    def criar_cinema(self, nome, endereco, capacidade):
        self.service.criar_cinema(nome, endereco, int(capacidade))

    def listar_cinemas(self):
        return self.service.listar_cinemas()
