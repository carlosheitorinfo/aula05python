#Crie uma classe Aluno com nome, nota e método resultado() que diga se passou (nota ≥ 7).

class Aluno:
    def __init__(self, aluno, nota):
        self.aluno = aluno
        self.nota = nota

    def resultado(self):
        if self.nota >= 7:
            return f"{self.aluno} foi aprovado!"
        else:
            return f"{self.aluno} foi reprovado!"

aluno1 = Aluno("Heitor", 9)
aluno2 = Aluno("Mario",5)

print(aluno1.resultado())
print(aluno2.resultado())

print(aluno1.resultado()," e ", aluno2.resultado())