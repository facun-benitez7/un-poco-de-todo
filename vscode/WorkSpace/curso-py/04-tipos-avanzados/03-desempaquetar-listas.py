numeros = [1, 2, 3]

# feo!
# primero = numeros[0]
# segundo = numeros[2]
# tercero = numeros[3]

primero, segundo, tercero = numeros
print(primero, segundo, tercero)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primero, segundo, *otros, ultimo = numeros
print(primero, segundo, otros, ultimo)
