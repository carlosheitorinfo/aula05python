class ContaBancaria:
    def __init__(self, titular,saldo):
        self.titular=titular
        self.__saldo=saldo

    def depositar(self,valor):
        self.__saldo+=valor

    def sacar(self, valor):
        if valor<=self.__saldo:
            self.__saldo-=valor
        else:
            print("saldo insuficiente.")
    
    def mostrar__saldo(self):
        print(f"Saldo atual: R$ {self.__saldo}")
    
titular=input("qual o seu nome? ")
print("1. saque", "2. deposito")
op=input(f" {titular} o que voce deseja fazer?")

if op=="1":
    def sacar(self, valor):
        valor=input(f"{titular}, Quanto vôce deseja sacar ?")
        def sacar(self, valor):
            if valor>=self.__saldo:
                self.__saldo-=valor
            else:
                print("saldo insuficiente.")

elif op=="2":
    saldo=input("quanto você deseja depositar? ")
    def depositar(self,valor):
        self.__saldo+=valor
        

titular=ContaBancaria(titular,saldo)
print(f"{titular}, o seu saldo inicial é de R$ {saldo}")

