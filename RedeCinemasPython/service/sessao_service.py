from datetime import datetime
from model.sessao import Sessao
from repository.sessao_repository import SessaoRepository
from repository.cinema_repository import CinemaRepository
from repository.filme_repository import FilmeRepository


class SessaoService:

    def __init__(self):
        self.repository = SessaoRepository()
        self.cinema_repo = CinemaRepository()
        self.filme_repo = FilmeRepository()

    def criar_sessao(self, cinema_id: int, filme_id: int,
                     data_hora: str, sala: str):
        # RN05: data deve ser futura
        dt = datetime.fromisoformat(data_hora)
        if dt <= datetime.now():
            raise ValueError("A data/hora da sessão deve ser futura.")

        cinema = self.cinema_repo.buscar_por_id(cinema_id)
        if not cinema:
            raise ValueError("Cinema não encontrado.")

        filme = self.filme_repo.buscar_por_id(filme_id)
        if not filme:
            raise ValueError("Filme não encontrado.")

        # RN02: verificar conflito de sala (intervalo de 30 min)
        sessoes_existentes = self.repository.sessoes_por_cinema(cinema_id)
        for s in sessoes_existentes:
            if s.sala != sala:
                continue
            dt_existente = datetime.fromisoformat(s.data_hora)
            filme_existente = self.filme_repo.buscar_por_id(s.filme_id)
            duracao_existente = filme_existente.duracao_min if filme_existente else 0
            fim_existente = dt_existente.timestamp() + (duracao_existente + 30) * 60
            inicio_nova = dt.timestamp()
            fim_nova = inicio_nova + (filme.duracao_min + 30) * 60
            inicio_existente = dt_existente.timestamp()
            if not (fim_nova <= inicio_existente or inicio_nova >= fim_existente):
                raise ValueError(
                    f"Conflito de horário na sala '{sala}'. "
                    "Respeite o intervalo mínimo de 30 minutos entre sessões."
                )

        sessao = Sessao(cinema_id, filme_id, data_hora, sala)
        self.repository.salvar(sessao)

    def listar_sessoes(self):
        return self.repository.listar()

    def buscar_por_id(self, sessao_id: int):
        return self.repository.buscar_por_id(sessao_id)

    def registrar_publico(self, sessao_id: int, publico: int):
        sessao = self.repository.buscar_por_id(sessao_id)
        if not sessao:
            raise ValueError("Sessão não encontrada.")

        cinema = self.cinema_repo.buscar_por_id(sessao.cinema_id)
        # RN03: público não pode exceder capacidade
        if publico > cinema.capacidade:
            raise ValueError(
                f"Público ({publico}) excede a capacidade do cinema ({cinema.capacidade})."
            )
        if publico < 0:
            raise ValueError("Público não pode ser negativo.")

        self.repository.atualizar_publico(sessao_id, publico)

    def total_publico_por_filme(self, filme_id: int) -> int:
        return self.repository.total_publico_por_filme(filme_id)

    def total_publico_por_cinema(self, cinema_id: int) -> int:
        return self.repository.total_publico_por_cinema(cinema_id)
