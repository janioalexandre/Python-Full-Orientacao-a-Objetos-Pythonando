class Pessoa: 

    def andar(self): 
        print("Estou andando")
    
    def falar(self): 
        print("Estou falando")

class Cliente(Pessoa): 

    def comprar(self): 
        print("Estou comprando")

class Vendedor(Pessoa): 

    def vender(self): 
        print("Estou vendendo")

c1 = Cliente()

c1.andar()
