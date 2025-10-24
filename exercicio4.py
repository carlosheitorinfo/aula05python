class Animal:
    def __init__(self, nome):
        self.nome = nome

class Cachorro(Animal):
    def falar(self):
        print(f"O {self.nome} faz Au Au!")

class Gato(Animal):
    def falar(self):
        print(f"O {self.nome} faz Miau!")

cachorro = Cachorro("cachorro")
cachorro.falar()  

gato = Gato("gato")
gato.falar() 