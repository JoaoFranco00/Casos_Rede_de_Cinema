class Genero:
    def __init__(self, nome: str, id: int = None):
        self.id = id
        self.nome = nome


class Diretor:
    def __init__(self, nome: str, nacionalidade: str = "", id: int = None):
        self.id = id
        self.nome = nome
        self.nacionalidade = nacionalidade


class Ator:
    def __init__(self, nome: str, nacionalidade: str = "", id: int = None):
        self.id = id
        self.nome = nome
        self.nacionalidade = nacionalidade
