import tkinter as tk
from tkinter import messagebox
import pandas as pd
import random

# Cargar preguntas desde el archivo Excel
file_path = "Preguntas.xlsx"
data = pd.read_excel(file_path)
data = data.astype(str)

# Función para iniciar el juego


def start_game():
    global question_index, correct_answers
    question_index = 0
    correct_answers = 0
    show_question()

# Función para mostrar la pregunta


def show_question():
    if question_index < len(data):
        # Obtener las opciones mezcladas
        options = [
            data["Respuesta Correcta"][question_index],
            data["R1"][question_index],
            data["R2"][question_index],
            data["R3"][question_index]
        ]
        random.shuffle(options)

        # Actualizar el texto de la pregunta y las opciones
        question_label.config(text=data["Pregunta"][question_index])
        for i in range(4):
            radio_buttons[i].config(text=options[i], value=options[i])

        # Reiniciar selección del usuario
        answer_var.set("")
        update_status()
    else:
        end_game()

# Actualizar estado del juego


def update_status():
    status_label.config(text=f"Pregunta {question_index + 1} de {len(data)}")

# Manejar respuesta del usuario


def handle_answer():
    global question_index, correct_answers

    # Validar si el usuario seleccionó una opción
    if not answer_var.get():
        messagebox.showwarning(
            "Atención", "Por favor selecciona una respuesta.")
        return

    if answer_var.get() == data["Respuesta Correcta"][question_index]:
        correct_answers += 1
    else:
        messagebox.showerror(
            "Respuesta Incorrecta", f"Incorrecto! La respuesta correcta era: {data['Respuesta Correcta'][question_index]}"
        )

    question_index += 1  # Pasar a la siguiente pregunta
    show_question()

# Finalizar el juego y mostrar puntaje


def end_game():
    messagebox.showinfo(
        "Fin del Juego", f"Has terminado! Respuestas correctas: {correct_answers} de {len(data)}")
    window.quit()


# Crear ventana principal
window = tk.Tk()
window.title("Juego de Trivia")

# Variables
question_index = 0
correct_answers = 0
answer_var = tk.StringVar()
answer_var.set("")  # Inicializar con un valor vacío

# Widgets
question_label = tk.Label(window, text="", wraplength=400, font=("Arial", 12))
question_label.pack(pady=(20, 10))

radio_buttons = []
for _ in range(4):
    rb = tk.Radiobutton(window, text="", variable=answer_var,
                        wraplength=300, font=("Arial", 10))
    rb.pack(anchor="w")
    radio_buttons.append(rb)

answer_button = tk.Button(window, text="Responder",
                          command=handle_answer, font=("Arial", 12))
answer_button.pack(pady=20)

status_label = tk.Label(window, text="", font=("Arial", 10))
status_label.pack()

# Iniciar el juego automáticamente
start_game()

# Correr la Aplicación
window.mainloop()
