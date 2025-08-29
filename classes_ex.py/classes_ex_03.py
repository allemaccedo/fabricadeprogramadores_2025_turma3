class Pessoa:
    def _init_(self, nome: str, nascimento: str, cpf: str, nome_pai: str, nome_mae: str,
 telefone: str, endereco: str, sexo: str, idade: int, altura: float):
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.nome_pai = nome_pai
        self.nome_mae = nome_mae
        self.telefone = telefone
        self.endereco = endereco
        self.sexo = sexo
        self._idade = idade
        self.altura = altura

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade: int):
        if nova_idade >= 0:
            self._idade = nova_idade

    def apresentar(self):
        print(f"Olá! Meu nome é {self.nome} e tenho {self._idade} anos.")

    def _contato(self):
        return f"Telefone: {self.telefone}, Endereço: {self.endereco}"

    def _maioridade(self):
        return self._idade >= 18

    def __mostrar_cpf(self):
        return f"CPF: {self.cpf}"

    def __dados_sigilosos(self):
        return f"Nome da mãe: {self.nome_mae}, Nome do pai: {self.nome_pai}"

    def exibir_dados_completos(self):
        print(self.__mostrar_cpf())
        print(self.__dados_sigilosos())