class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def logar_sistema(self):
        print(f'{self.nome} logou no sistema.')

p1 = Pessoa('Janio', 39, '123.456.789-00')
p2 = Pessoa('Alexandre', 30, '987.654.321-00')

p1.logar_sistema()
p2.logar_sistema()