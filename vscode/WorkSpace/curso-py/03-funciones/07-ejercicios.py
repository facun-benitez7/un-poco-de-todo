def sin_espacio(texto):
    texto = texto.lower()
    espacio = " "
    for _ in texto:
        if _ == espacio:
            texto = texto.replace(" ", "")
    return texto


def alreve(texto):
    textito = sin_espacio(texto)
    copia = ""
    resultado = len(textito)
    indice = resultado - 1
    for _ in range(resultado):
        copia = f"{copia}{textito[indice]}"
        indice = indice-1
    return copia


def es_palindromo(texto):
    if sin_espacio(texto) == alreve(texto):
        return True
    else:
        return False


print("Menem", es_palindromo("Menem"))
print("Reconocer", es_palindromo("Reconocer"))
print("Amo la paloma", es_palindromo("Amo la paloma"))
print("Hola mundo", es_palindromo("Hola mundo"))
