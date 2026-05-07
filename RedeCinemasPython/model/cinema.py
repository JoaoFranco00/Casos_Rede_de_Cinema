class Cinema:
    def __init__(self, nome: str, endereco: str, capacidade: int, id: int = None):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.capacidade = capacidade
