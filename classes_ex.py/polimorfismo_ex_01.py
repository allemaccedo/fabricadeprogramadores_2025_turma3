from heranca_ex__01 import Personagem

class Naruto(Personagem):
    def descrever(self):
        print(f"Sou {self.nome}, um ninja de {self.nacionalidade}, tenho {self.idade} anos. "
              f"Minha habilidade especial é {self.habilidade} e minha cor preferida é {self.cor}.")

personagens = [
    Naruto("Sasuke Uchiha", "Konoha", 17, "Sharingan e Chidori", "Azul"),
    Naruto("Obito Uchiha", "Konoha", 31, "Mangekyou Sharingan e Kamui", "Laranja"),
    Naruto("Minato Namikaze", "Konoha", 24, "Hiraishin (Técnica do Deus Voador do Trovão)", "Amarelo"),
    Naruto("Madara Uchiha", "Konoha", 90, "Eternal Mangekyou Sharingan e Rinnegan", "Vermelho"),
    Naruto("Itachi Uchiha", "Konoha", 21, "Amaterasu e Tsukuyomi", "Preto"),
    Naruto("Kakashi Hatake", "Konoha", 30, "Sharingan e Chidori (Raikiri)", "Cinza"),
]

for p in personagens:
    p.descrever()
    