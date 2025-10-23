class Animal:
    def emitir_som(self):
        print("som genérico")

class Cachorro(Animal):
    def emitir_som(self):
        print("auau")

class Gato(Animal):
    def emitir_som(self):
        print("miau")

animais=[Cachorro(), Gato(), Animal()]

for a in animais:
    a.emitir_som()
