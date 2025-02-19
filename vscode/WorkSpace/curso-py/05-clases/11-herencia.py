class Animal:
    def comer(self):
        print("comiendo")


class Perro(Animal):
    def pasear(self):
        print("paseando")


class Chanchito(Perro):
    def programar(self):
        print("programando")


chanchito = Chanchito()
perro = Perro()
perro.comer()
