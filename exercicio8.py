#8. Crie uma classe Calculadora com métodos somar, subtrair, multiplicar, dividir.

class Calculadora:
    def somar(self, n1, n2):
        return n1 + n2
    def subtrair(self, n1, n2):
        return n1 - n2
    def multiplicar(self, n1, n2):
        return n1 * n2
    def dividir(self, n1, n2):
        if n2== 0:
            return "Erro: Divisão por zero não é permitida."
        return n1 / n2

calculo = Calculadora()

print("1. somar", "2. subtrair, 3. multiplicar, 4. dividir")
op=int(input("Qual operação matemática vôce deseja fazer?"))
n1=float(input("digite o primeiro número: "))
n2=float(input("digite o segundo número: "))

if op==1:
    print(f"{n1} + {n2} = {calculo.somar(n1,n2)}")
elif op==2:
    print(f"{n1} - {n2} = {calculo.subtrair(n1, n2)}")
elif op==3:
    print(f"{n1} * {n2} = {calculo.multiplicar(n1,n2)}")
elif op==4:
    print(f"{n1} / {n2} = {calculo.dividir(n1,n2)}")

