class Marinhos:
    def __init__(self, nome, tipo, especie, tamanho, alimentacao):
        self.nome = nome
        self.tipo = tipo
        self.especie = especie  
        self.tamanho = tamanho
        self.alimentacao = alimentacao

    def nadar(self):
        return print(f"O {self.nome} está nadando.")

    def alimentar(self):
        return print(f"O {self.nome} se alimenta de {self.alimentacao}.")

    def descrever(self):
        return print(f"{self.nome} é um {self.tipo} da espécie {self.especie}, "
                f"tem porte {self.tamanho} e alimentação {self.alimentacao}.")

    def dormir(self):
        return print(f"O {self.nome} está descansando.")

    def emitir_som(self):
        return print(f"O {self.nome} emite sons característicos da sua espécie.")

animais = Marinhos("Golfinho", "Mamífero", "boto-cor-de-rosa", "Médio", "Carnívoro")
animais.descrever()