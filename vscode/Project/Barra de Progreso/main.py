import tkinter as tk
from tkinter import ttk

# Funcion para incrementar barra de progreso manualmente


def incrementar_barra():
    valor = barra_progreso["value"]
    if valor < 100:
        barra_progreso["value"] = valor + 10
        actualizar_porcentaje()

# Funcion para incrementar barra de progreso automaticamente


def completar_barra():
    valor = barra_progreso["value"]
    if valor < 100:
        barra_progreso["value"] = valor + 5
        actualizar_porcentaje()
        ventana.after(100, completar_barra)

# Funcion para resetear la barra de progreso


def resetear_barra():
    barra_progreso["value"] = 0
    actualizar_porcentaje()


def actualizar_porcentaje():
    valor = barra_progreso["value"]
    porcentaje.set(f"{int(valor)}%")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Barra de Progreso con Tkinter")
ventana.geometry("300x250")
ventana.configure(bg="#2C3E50")

# Estilo de la barra de progreso y los botones
style = ttk.Style()
style.theme_use("clam")

# Estilo para la barra de progreso
style.configure("TProgressbar", troughcolor="#34495E",
                background="#1ABC9C", thickness=20)

# Estilo para los botones
style.configure("TButton", font=("Helvetica", 10, "bold"),
                background="#2980D9", foreground="white")
style.map("TButton", background=[("active", "#3498DB")])


barra_progreso = ttk.Progressbar(ventana, orient="horizontal", length=200,
                                 mode="determinate", style="TProgressbar")
barra_progreso.pack(pady=20)

porcentaje = tk.StringVar()
porcentaje.set("0%")

etiqueta_porcentaje = tk.Label(ventana, textvariable=porcentaje, font=(
    "Helvetica", 10, "bold"), bg="#2C3E50", fg="white")
etiqueta_porcentaje.pack(pady=10)

boton_incrementar = ttk.Button(
    ventana, text="Incrementar", command=incrementar_barra, style="TButton")
boton_incrementar.pack(pady=5)

boton_completar = ttk.Button(
    ventana, text="Completar", command=completar_barra, style="TButton")
boton_completar.pack(pady=5)

boton_resetear = ttk.Button(
    ventana, text="Resetear", command=resetear_barra, style="TButton")
boton_resetear.pack(pady=5)

ventana.mainloop()
