#5. Crie uma classe Produto com atributos nome e preço. Crie um método desconto(percentual).

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
            valor_desconto = self.preco * (percentual/100)
            novo_preco = self.preco - valor_desconto
            return novo_preco

produto1=input("Diga o nome do produto: ") 
preco=float(input("Qual o valor do produto? "))   
produto1 = Produto(produto1,preco)
print(f"Preço original do {produto1.nome}: R${produto1.preco:.2f}")
if preco<= 50:
    percentual=10
else:
    percentual=15
    
novo_preco= produto1.desconto(percentual)
print(f"Preço do {produto1.nome} com {percentual} % de desconto: R${novo_preco:.2f}")

