class MiError(Exception):
    "Esta clase es para representar mi Error!"

    def __init__(self, mensaje, codigo):
        self.mensaje = mensaje
        self.codigo = codigo

    def __str__(self):
        return f"{self.mensaje} - codigo: {self.codigo}"


def division(n=0):
    if n == 0:
        raise MiError("No se puede dividir por 0", 8005)
    return 5 / n


try:
    division()
except MiError as e:
    print(e)
