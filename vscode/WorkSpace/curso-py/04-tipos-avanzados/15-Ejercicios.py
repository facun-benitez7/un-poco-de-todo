# 1. Eliminar los espacios en blanco de un string
# y devolver una lista con los caracteres restantes
# 2. Contar en un diccionario cuanto se repiten
# los caracteres de un string
# 3. Ordenar las llaves de un diccionario
# por el valor que tienen y devolver una lista
# que contiene tuplas [("a", 3), ("b", 2), ("c", 4), ("d", 4)]
# 4. De un listado de tuplas, devolver las tuplas
# que tengan el mayor valor.
# [("a", 3), ("b", 2), ("c", 4), ("d", 4)] -> [("c", 4), ("d", 4)]
# 5. Crear un mensaje que diga:
# Los caracteres que mas se repiten con 4 repeticiones son:
# - C
# - D

# 6. Juntar las soluciones de los ejercicios anteriores
# para econtrar los caracteres que mas se repiten
# de un string.

oracion = input("Ingrese el String: ")


# def eliminar_espacios(cadena):
#     cadena_sin_espacios = cadena.replace(" ", "")
#     lista_de_caracteres = list(cadena_sin_espacios)
#     return lista_de_caracteres


# print(eliminar_espacios(oracion))

def contador_de_caracteres(cadena):
    diccionario_contador = {}
    for char in cadena:
        if char in diccionario_contador:
            diccionario_contador[char] += 1
        else:
            diccionario_contador[char] = 1
    return diccionario_contador


# def ordenar_por_valor(diccionario):
#     lista_ordenada = sorted(diccionario.items(),
#                             key=lambda item: item[1], reverse=True)
#     return lista_ordenada

def cuatro_caracteres(diccionario):
    for llave, valor in diccionario.items():
        if valor == 4:
            print(llave.capitalize())


def maximos(diccionario):
    letra1 = ""
    letra2 = ""
    max1 = 0
    max2 = 0
    for llave, valor in diccionario.items():
        if valor > max1:
            max2 = max1
            max1 = valor
            letra2 = letra1
            letra1 = llave
        elif valor > max2:
            max2 = valor
            letra2 = llave
    print(f"Los 2 caracteres que mas se repiten son: {letra1} y {letra2}")


maximos(contador_de_caracteres(oracion))
