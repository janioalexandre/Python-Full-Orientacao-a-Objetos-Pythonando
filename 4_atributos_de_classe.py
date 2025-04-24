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

p1 = Pessoa('Janio', 39)
p2 = Pessoa('Alexandre', 30)

p1.possui_boca = False

print(p1.nome)
print(p2.nome)


print(p1.possui_boca)
print(p2.possui_boca)