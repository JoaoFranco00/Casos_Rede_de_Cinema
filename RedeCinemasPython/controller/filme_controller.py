from service.filme_service import FilmeService


class FilmeController:

    def __init__(self):
        self.service = FilmeService()

    def criar_filme(self, titulo, duracao_min, sinopse, generos_str,
                    diretores_str, atores_str):
        generos = [g.strip() for g in generos_str.split(",") if g.strip()]
        diretores = [d.strip() for d in diretores_str.split(",") if d.strip()]
        atores = [a.strip() for a in atores_str.split(",") if a.strip()]
        self.service.criar_filme(titulo, int(duracao_min), sinopse,
                                 generos, diretores, atores)

    def listar_filmes(self):
        return self.service.listar_filmes()
