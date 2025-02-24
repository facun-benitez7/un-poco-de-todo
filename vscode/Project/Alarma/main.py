import time
import pygame
import sys

# Inicializar pygame
pygame.init()
pygame.mixer.init()  # Inicializar el módulo de sonido una sola vez

# Configuración de la pantalla
ANCHO_PANTALLA = 640
ALTO_PANTALLA = 480

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Fuente
fuente = pygame.font.Font(None, 74)

pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Temporizador de Alarma")


def mostrar_tiempo_restante(segundos_restantes):
    pantalla.fill(NEGRO)
    minutos_restantes = segundos_restantes // 60
    # Aquí corregimos el doble guion bajo
    segundos_restantes = segundos_restantes % 60
    tiempo_formateado = f"{minutos_restantes:02d}:{segundos_restantes:02d}"
    texto = fuente.render(tiempo_formateado, True, BLANCO)
    rect_texto = texto.get_rect(
        center=(ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2))
    pantalla.blit(texto, rect_texto)
    pygame.display.flip()


def alarma(segundos):
    tiempo_inicial = time.time()

    while True:
        tiempo_actual = time.time()
        tiempo_transcurrido = tiempo_actual - tiempo_inicial
        segundos_restantes = int(segundos - tiempo_transcurrido)

        if segundos_restantes <= 0:
            break  # Sale del bucle cuando el tiempo llega a 0

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        mostrar_tiempo_restante(segundos_restantes)
        pygame.time.delay(1000)  # Reemplaza time.sleep(1)

    # Reproducir el sonido de la alarma
    try:
        pygame.mixer.music.load(
            "C:/Users/facuu/OneDrive/Documents/vscode/Project/Alarma/Alarma.mp3")
        pygame.mixer.music.play()
    except pygame.error:
        print("Error al cargar el archivo de audio.")

    while pygame.mixer.music.get_busy():
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.time.delay(1000)  # Reemplaza time.sleep(1)


# Pedir tiempo al usuario con validación
while True:
    try:
        minutos = int(input("Ingrese minutos: "))
        segundos = int(input("Ingrese segundos: "))
        if minutos < 0 or segundos < 0:
            print("Por favor, ingrese valores positivos.")
        else:
            break
    except ValueError:
        print("Ingrese solo números enteros.")

segundos_totales = minutos * 60 + segundos
alarma(segundos_totales)
