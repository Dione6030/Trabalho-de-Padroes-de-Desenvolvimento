class EncomendaSimples:
    def __init__(self, descricao, peso):
        self.descricao = descricao
        self.peso = peso

    def get_peso(self):
        return self.peso


class PacoteEncomendas:
    def __init__(self, nome):
        self.nome = nome
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def get_peso_total(self):
        total = 0
        for item in self.itens:
            if isinstance(item, EncomendaSimples):
                total += item.get_peso()
            elif isinstance(item, PacoteEncomendas):
                total += item.get_peso_total()
        return total

e1 = EncomendaSimples("Livro", 1.2)
e2 = EncomendaSimples("Notebook", 2.5)

pacote = PacoteEncomendas("Pacote Principal")
pacote.adicionar(e1)
pacote.adicionar(e2)

print("Peso total:", pacote.get_peso_total(), "kg")