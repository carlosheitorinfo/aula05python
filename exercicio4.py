#Crie uma classe Animal com método falar().

class Animal: ('')
   
class Cachorro(Animal):
    def falar(self):
        print("O cachorro faz auau !!")

class Gato(Animal):
    def falar(self):
        print("O Gato faz miau !!")

animais = [Cachorro(), Gato()]

for animal in animais:
    animal.falar()