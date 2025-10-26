class Funcionario:
    def __init__(self, nome, setor):
        self.nome = nome
        self.setor = setor
        
class Gerente (Funcionario):
    def __init__(self, nome, setor, funcao):
        super().__init__(nome, setor)
        self.funcao = funcao
       

funcionario1 = Funcionario("Mario", "produção")
gerente1 = Gerente("Heitor", "Gerencia", "Gerente Master")

empresa = [Funcionario(), Gerente()]
print({empresa})