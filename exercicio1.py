class Pessoa:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade

    def msg(self):
        print(f"Olá, meu {self.nome} e tenho {self.idade}")

eu=Pessoa("Heitor", 50)
eu.msg()


