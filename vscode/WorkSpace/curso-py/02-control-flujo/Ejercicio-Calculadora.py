print("""
Bienvenidos a la calculadora
Para salir escribe 'salir'
Las operaciones son suma, multi, div y resta.
""")

operacion = ""
resultado = 0

while operacion.lower() != "salir":
    numero1 = float(input("Ingresa el numero: "))
    operacion = input("Ingresa la operacion: ")
    numero2 = float(input("Ingresa el segundo numero: "))
    if operacion.lower() == "suma":
        resultado = numero1 + numero2
        print("El resultado es: ", resultado)
    elif operacion.lower() == "multi":
        resultado = numero1 * numero2
        print("El resultado es: ", resultado)
    elif operacion.lower() == "div":
        resultado = numero1 / numero2
        print("El resultado es: ", resultado)
    elif operacion.lower() == "resta":
        resultado = numero1 - numero2
        print("El resultado es: ", resultado)
    elif operacion.lower() == "salir":
        print("Gracias por utilizar esta calculadora!")
        break
    else:
        print("La operacion ingresada no es valida, trate nuevamente.")
