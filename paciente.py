class Paciente:

    def __init__(self, nome, registro, idade):
        self.nome = nome
        self.registro = registro
        self.idade = idade

    def __str__(self):
        return (
            f"\nNome: {self.nome}"
            f"\nRegistro: {self.registro}"
            f"\nIdade: {self.idade}"
        )