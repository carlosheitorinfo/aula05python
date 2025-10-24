class Carro:
    def __init__(self, modelo, ano):
        self.modelo=modelo
        self.ano=ano
        self.velocidade=0

    def acelerar(self):
        self.velocidade += 10
        print(f" A {self.modelo} modelo {self.ano} está a {self.velocidade} km/h")

    def frear(self):
        print(f"A {self.modelo} modelo {self.ano} reduziu para {self.velocidade} km/h")

carro1 = Carro("Ferrari", 2000)
carro1.acelerar()
carro1.frear()
