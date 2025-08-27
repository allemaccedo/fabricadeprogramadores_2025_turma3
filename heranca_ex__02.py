from heranca_ex__01 import Personagem

class Nacionalidade():

    def descrever(self):
        return print(f"o {self.nome} nasceu em {self.nacionalidade}")
    
Personagem2 = Personagem ("Naruto Uzumaki", "Konohagakure(Vila Oculta da Folha)", 17, "Rasengan", "Laranja")
Personagem2.descrever()