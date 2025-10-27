#1. Crie uma classe Pessoa com os atributos nome e idade. 
# Crie um método que exiba uma mensagem: “Olá, meu nome é [nome] e tenho [idade] anos.”

class Pessoa:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade

    def msg(self):
        print(f"Olá, meu {self.nome} e tenho {self.idade}")

eu=Pessoa("Heitor", 50)
eu.msg()


