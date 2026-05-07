from service.sessao_service import SessaoService
from service.cinema_service import CinemaService
from service.filme_service import FilmeService


class SessaoController:

    def __init__(self):
        self.service = SessaoService()
        self.cinema_service = CinemaService()
        self.filme_service = FilmeService()

    def criar_sessao(self, cinema_id, filme_id, data_hora, sala):
        self.service.criar_sessao(int(cinema_id), int(filme_id), data_hora, sala)

    def listar_sessoes(self):
        return self.service.listar_sessoes()

    def registrar_publico(self, sessao_id, publico):
        self.service.registrar_publico(int(sessao_id), int(publico))

    def total_por_filme(self, filme_id):
        return self.service.total_publico_por_filme(int(filme_id))

    def total_por_cinema(self, cinema_id):
        return self.service.total_publico_por_cinema(int(cinema_id))

    def listar_cinemas(self):
        return self.cinema_service.listar_cinemas()

    def listar_filmes(self):
        return self.filme_service.listar_filmes()
