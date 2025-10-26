#Crie uma classe Retangulo com base e altura e método area().

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

base=float(input("digite um valor para a base do retangulo: "))
altura=float(input("digite um valor para a altura do retangulo: "))
medidas_retangulo = Retangulo(base,altura)
area_retangulo = medidas_retangulo.area()
print(f"O retangulo com {base} de base e {altura} de altura tem uma área de {area_retangulo}")