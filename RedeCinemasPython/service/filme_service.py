from model.filme import Filme
from repository.filme_repository import FilmeRepository


class FilmeService:

    def __init__(self):
        self.repository = FilmeRepository()

    def criar_filme(self, titulo: str, duracao_min: int, sinopse: str,
                    generos: list, diretores: list, atores: list):
        if not titulo:
            raise ValueError("Título é obrigatório.")
        if duracao_min < 60:
            raise ValueError("Duração mínima do filme é 60 minutos.")
        if not generos:
            raise ValueError("Informe pelo menos um gênero.")
        if not diretores:
            raise ValueError("Informe pelo menos um diretor.")
        if not atores:
            raise ValueError("Informe pelo menos um ator.")

        filme = Filme(titulo, duracao_min, sinopse,
                      generos=generos, diretores=diretores, atores=atores)
        self.repository.salvar(filme)

    def listar_filmes(self):
        return self.repository.listar()

    def buscar_por_id(self, filme_id: int):
        return self.repository.buscar_por_id(filme_id)
