from heranca_ex__01 import Personagem

class AnimalMarinho:
    def _init_(self, nome):
        self.nome = nome
    
    def descrever(self):
        print(f"Eu sou um animal marinho chamado {self.nome}, e vivo no oceano.")

class Pessoa:
    def _init_(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def descrever(self):
        print(f"Eu sou {self.nome}, tenho {self.idade} anos e sou uma pessoa comum.")


objetos = [
    Personagem("Naruto Uzumaki", "Konoha", 17, "Rasengan", "Laranja"),
    AnimalMarinho("Golfinho"),
    Pessoa("João", 20),
    Personagem("Sasuke Uchiha", "Konoha", 17, "Chidori", "Azul"),
    AnimalMarinho("Tubarão")
]

for obj in objetos:
    obj.descrever()