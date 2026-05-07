from model.cinema import Cinema
from repository.cinema_repository import CinemaRepository


class CinemaService:

    def __init__(self):
        self.repository = CinemaRepository()

    def criar_cinema(self, nome: str, endereco: str, capacidade: int):
        if not nome or not endereco:
            raise ValueError("Nome e endereço são obrigatórios.")
        if capacidade <= 0:
            raise ValueError("Capacidade deve ser maior que zero.")
        cinema = Cinema(nome, endereco, capacidade)
        self.repository.salvar(cinema)

    def listar_cinemas(self):
        return self.repository.listar()

    def buscar_por_id(self, cinema_id: int):
        return self.repository.buscar_por_id(cinema_id)
