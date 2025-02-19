import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow
import pygame  # pip install pygame

# Inicializar pygame para la reproduccion de sonido
pygame.mixer.init()

# Crear la ventana principal
root = tk.Tk()
root.title("El Barto")
root.geometry("400x600")  # Tamaño inicial

# Cargar la imagen original
ruta_imagen = "F:/vscode/Project/ElBarto/Barto.jpg"
imagen_original = Image.open(ruta_imagen)

# Crear una variable global para la imagen de fondo
imagen_fondo_global = None

# Crear un Label para la imagen de fondo
fondo_label = tk.Label(root)
fondo_label.place(relwidth=1, relheight=1)  # Rellenar toda la ventana

# Funcion para redimensionar el fondo


def redimensionar_fondo(event):
    """Redimensiona la imagen de fondo cuando cambia el tamaño de la ventana."""
    global imagen_fondo_global  # Mantener referencia de la imagen

    nuevo_ancho = event.width
    nuevo_alto = event.height

    # Redimensionar la imagen manteniendo la calidad
    imagen_redimensionada = imagen_original.resize(
        (nuevo_ancho, nuevo_alto), Image.LANCZOS)
    imagen_fondo_global = ImageTk.PhotoImage(imagen_redimensionada)

    # Actualizar la imagen del Label
    fondo_label.config(image=imagen_fondo_global)


# Vincular el evento de cambio de tamaño de la ventana
root.bind("<Configure>", redimensionar_fondo)

# Cargar la imagen del botón en forma de nube
# Debe ser PNG con fondo transparente
ruta_imagen = "F:/vscode/Project/ElBarto/Nube.png"
imagen_nube = Image.open(ruta_imagen)
# Ajustar tamaño si es necesario
imagen_nube = imagen_nube.resize((120, 80), Image.LANCZOS)
imagen_nube = ImageTk.PhotoImage(imagen_nube)

# Crear el botón con la imagen
boton_nube = tk.Button(root, image=imagen_nube, text="¡Ay Caramba!", font=("Simpsonfont", 12, "bold"), fg="#2e86c1", compound="center", borderwidth=0,
                       highlightthickness=0, bg="#0e0a09", activebackground="white")
boton_nube.place(relx=0.5, rely=0.1, anchor="center")  # Centrar el botón

# Mantener la referencia de la imagen
boton_nube.image = imagen_nube

# Funcion para reproducir el audio


def reproducir_audio():
    # Ruta del archivo de audio
    pygame.mixer.music.load("F:/vscode/Project/ElBarto/¡Ay Caramba!.mp3")
    pygame.mixer.music.play()  # Reproducir el audio


# Asociar la función de reproducción de audio al evento de clic del botón
boton_nube.config(command=reproducir_audio)

# Ejecutar la aplicación
root.mainloop()
