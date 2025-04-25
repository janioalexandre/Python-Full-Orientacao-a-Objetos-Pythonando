class Pessoa:
    possui_olho = True
    possui_boca = True
    raca = 'Ser humano'

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def retorna_nome(self):
        return self.nome
    
    def logar_sistema(self):
        print(f'{self.retorna_nome()} Está logado no sistema.')

    @classmethod
    def andar(cls, velocidade):
        print(f'Estou andando na velocidade {velocidade} km/h.')

# p1 = Pessoa('Janio', 39)
# p2 = Pessoa('Alexandre', 30)

Pessoa.andar(10)