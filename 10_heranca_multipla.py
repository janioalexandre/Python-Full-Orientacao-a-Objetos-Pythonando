class Animal:
    def andar(self):
        print("estou andando")
    
    def correr(self):
        print("estou correndo")
    
    def pular(self):
        print("estou pulando")

class Felino(Animal):
    def felino(self):
        print("eu sou um felino")

class Gato(Felino):
    def miar(self):
        print("estou miando")

class Cachorro(Animal):
    def latir(self):
        print("estou latindo")

y = Gato()
y.andar()