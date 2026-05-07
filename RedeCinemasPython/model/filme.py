class Filme:
    def __init__(self, titulo: str, duracao_min: int, sinopse: str = "",
                 id: int = None, generos=None, diretores=None, atores=None):
        self.id = id
        self.titulo = titulo
        self.duracao_min = duracao_min
        self.sinopse = sinopse
        self.generos = generos or []
        self.diretores = diretores or []
        self.atores = atores or []
