numeros = [1, 4, 8, 6, 7, 2]

# numeros.sort(reverse=True) #Los ordena y los imprime al reves
numeros2 = sorted(numeros)  # los ordena pero crea una lista nueva
print(numeros2)
print(numeros)

usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

usuarios.sort(key=lambda el: el[1])
print(usuarios)
