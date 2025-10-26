class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
            valor_desconto = self.preco * 0.10
            novo_preco = self.preco - valor_desconto
            return novo_preco
       
produto1 = Produto("Notebook", 2500.00)
print(f"Preço original do {produto1.nome}: R${produto1.preco:.2f}")
novo_preco_com_desconto = produto1.desconto(10)
print(f"Preço do {produto1.nome} com 10% de desconto: R${novo_preco_com_desconto:.2f}")

