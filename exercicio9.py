#Crie uma classe Funcionario e uma classe Gerente que herda de Funcionario e adiciona o atributo setor.

class Funcionario:
    def __init__(self, nome, setor):
        self.nome = nome
        self.setor = setor

    def exibir_informacoes(self):
        return f"Nome: {self.nome}, Setor: {self.setor}"
        
class Gerente (Funcionario):
    def __init__(self, nome, setor, funcao):
        super().__init__(nome, setor)
        self.funcao = funcao

    def exibir_informacoes(self):
        info_funcionario = super().exibir_informacoes()
        return f"{info_funcionario}, Função: {self.funcao}"

funcionario1 = Funcionario("Mario", "produção")
gerente1 = Gerente("Heitor", "Gerencia", "Gerente Master")

print(funcionario1.exibir_informacoes())
print(gerente1.exibir_informacoes())