try:
    n1 = int(input("Ingresa primer numero: "))
except Exception as e:
    print("Ocurrio un error!")
else:
    print("No ocurrio ningun error!")
finally:
    print("se ejecuta siempre!")
