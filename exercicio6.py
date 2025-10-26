#Crie uma classe Livro com título, autor e método exibir_detalhes().

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo  
        self.autor = autor   
    
    def exibir_detalhes(self):
        print(f"Título: {self.titulo}, escrito por {self.autor}")
       

livro1 = Livro("O Livro dos Espíritos","Allan Kardek")

livro1.exibir_detalhes()

