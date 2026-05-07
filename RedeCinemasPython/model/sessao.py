class Sessao:
    def __init__(self, cinema_id: int, filme_id: int, data_hora: str,
                 sala: str, publico: int = 0, id: int = None,
                 cinema_nome: str = "", filme_titulo: str = ""):
        self.id = id
        self.cinema_id = cinema_id
        self.filme_id = filme_id
        self.data_hora = data_hora
        self.sala = sala
        self.publico = publico
        # campos de display (join)
        self.cinema_nome = cinema_nome
        self.filme_titulo = filme_titulo
