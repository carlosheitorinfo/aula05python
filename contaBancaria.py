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

conta1 = ContaBancaria("Heitor", 7000)
conta1.mostrar__saldo()
conta1.depositar(4000)
conta1.mostrar__saldo()   
                        
                        

