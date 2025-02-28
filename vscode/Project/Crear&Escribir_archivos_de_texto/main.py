# -*- coding: utf-8 -*-

def escribir_archivo(nombre_archivo, contenido):
    with open(nombre_archivo, "w") as archivo:
        archivo.write(contenido)


def obtener_entrada_usuario():
    print("\nIntroduce texto (escribe GUARDAR en una nueva linea para salir): ")

    lineas = []
    while True:
        linea = input()
        if linea == "GUARDAR":
            break
        lineas.append(linea)

    return "\n".join(lineas)


def main():
    nombre_archivo = input("Introduce el nombre del archivo a crear: ").strip()
    try:
        nuevo_contenido = obtener_entrada_usuario()
        escribir_archivo(nombre_archivo, nuevo_contenido)
        print(f"\Archivo {nombre_archivo} creado correctamente")

    except OSError:
        print(f"\nNo se puede crear el archivo {nombre_archivo}")


if __name__ == "__main__":
    main()
