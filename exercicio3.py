class ContaBancaria:

    def __init__(self):
        self.titular = ""
        self.__saldo = 0

    def sacar(self, valor):
        print(f"valor é: R$ {valor} e o saldo é {self.__saldo}")
        if self.__saldo>=valor:
            self.__saldo-=valor
            print(f"O saque foi de R$ {valor}. O saldo atual é R${self.__saldo}")
        else:
            print("saldo insuficiente.")

    def depositar(self,valor):
        self.__saldo+=valor

    def mostrar_saldo(self):        
        if(self.__saldo == None):
            print("Seu saldo está zerado")
        else:
            print(f"Saldo atual: R$ {self.__saldo}")

print("-"*30)
cliente = ContaBancaria()

cliente.titular = input('Digite o seu nome: ')
print(f"Seja bem-vindo(a) {cliente.titular}! O sue saldo atual é {cliente.mostrar_saldo()} ")


print("1. saque", "2. deposito, 3. saldo")
op=int(input(f" {cliente.titular} o que voce deseja fazer?"))

if(op==1):
    valor = float(input("Digite o valor a ser sacado: "))
    resultado = cliente.sacar(valor)
    
elif(op==2):
    valor = float(input("Digite o valor a ser depositado: "))
    resultado = cliente.depositar(valor)
    print(resultado)
elif(op==3):
    print(f"Seu saldo atual é: R${cliente.mostrar_saldo()}")