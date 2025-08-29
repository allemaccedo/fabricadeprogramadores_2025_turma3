class Personagem():
    def __init__(self, nome, nacionalidade, idade, habilidade, cor): 

        self.nome = nome 
        self.nacionalidade = nacionalidade 
        self.idade = idade 
        self.habilidade = habilidade
        self.cor = cor

    def nome(self):
        return print(f"opa, sou o {self.nome}")
    
    def nacionalidade(self):
        return print(f"eu sou d {self.nacionalidade}")
    
    def descrever(self):
        return print(f"Ola,eu sou {self.nome},sou Hokage de {self.nacionalidade}, e nasci em {self.nacionalidade},minha idade e {self.idade} anos, "
                f"minha habilidade especial é o {self.habilidade} e minha cor preferida é {self.cor}")
    
    def idade(self):
        return print(f"tenho {self.idade} anos")
    
    def habilidade(self):
        return print(f"minha habilidade especial è {self.habilidade}")
    
    def cor(self):
        return print (f"minha cor é {self.cor}")
    
Personagem1 = Personagem ("Naruto Uzumaki", "Konohagakure (Vila Oculta da Folha)", 17, "Rasengan", "Laranja")
Personagem1.descrever()