from abc import ABC, abstractmethod

class ComponenteEncomenda(ABC):
    @abstractmethod
    def get_peso(self):
        pass

    @abstractmethod
    def exibir(self, nivel=0):
        pass

class EncomendaSimples(ComponenteEncomenda):
    def __init__(self, descricao, peso):
        self.descricao = descricao
        self.peso = peso

    def get_peso(self):
        return self.peso

    def exibir(self, nivel=0):
        print("  " * nivel + f"- Encomenda: {self.descricao} ({self.peso} kg)")


class PacoteEncomendas(ComponenteEncomenda):
    def __init__(self, nome):
        self.nome = nome
        self.itens = []

    def adicionar(self, componente: ComponenteEncomenda):
        self.itens.append(componente)

    def get_peso(self):
        return sum(item.get_peso() for item in self.itens)

    def exibir(self, nivel=0):
        print("  " * nivel + f"[Pacote] {self.nome}")
        for item in self.itens:
            item.exibir(nivel + 1)


e1 = EncomendaSimples("Livro", 1.2)
e2 = EncomendaSimples("Notebook", 2.5)
e3 = EncomendaSimples("Mouse Gamer", 0.3)

pacote_secundario = PacoteEncomendas("Pacote Secundário")
pacote_secundario.adicionar(e3)

pacote_principal = PacoteEncomendas("Pacote Principal")
pacote_principal.adicionar(e1)
pacote_principal.adicionar(e2)
pacote_principal.adicionar(pacote_secundario)

pacote_principal.exibir()
print("Peso total:", pacote_principal.get_peso(), "kg")