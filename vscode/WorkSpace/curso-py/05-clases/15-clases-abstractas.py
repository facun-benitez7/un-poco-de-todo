from abc import ABC, abstractmethod


class Model(ABC):
    @property
    @abstractmethod
    def tabla(self):
        pass

    @abstractmethod
    def guardar(self):
        pass

    @classmethod
    def buscar_por_id(self, _id):
        print(f"buscando por id {_id} en la tabla {self.tabla} ")


class Usuario(Model):
    tabla = "Usuario"

    def guardar(self):
        print("guardando usuario")


usuario = Usuario()
usuario.guardar()
usuario.buscar_por_id(123)

model = Model()
