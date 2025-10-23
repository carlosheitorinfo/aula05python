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
    
cliente= ContaBancaria()
cliente.titular=input("qual o seu nome?")
saldo=input("quanto você deseja depositar")
print(f"{cliente.titular}, o seu saldo inicial é de {saldo}")

