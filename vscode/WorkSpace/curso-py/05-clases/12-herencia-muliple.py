class Caminador:
    def caminar(self):
        print("caminando")


class Volador:
    def volar(self):
        print("volando")


class Nadador:
    def nadar(self):
        print("nadando")


class Pato(Volador, Caminador, Nadador):
    def programar(self):
        print("programando")


patito = Pato()
patito.caminar()
