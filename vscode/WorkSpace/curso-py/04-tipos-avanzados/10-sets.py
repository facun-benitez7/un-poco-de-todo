# set significa grupo o conjunto
primer = {1, 1, 2, 2, 3, 4}
# primer.add(5)
# primer.remove(1)
segundo = [3, 4, 5]
segundo = set(segundo)

# print(primer | segundo)  # Union
# print(primer & segundo)  # interseccion
# print(primer - segundo)  # diferencia
print(primer ^ segundo)  # diferencia simetrica

if 5 in segundo:
    print("Hola Mundo!")
