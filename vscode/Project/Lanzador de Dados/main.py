import tkinter as tk
import random
from tkinter import scrolledtext


def roll_dice(num_dice, die_type):
    return [random.randint(1, die_type) for _ in range(num_dice)]


def on_roll():
    num_dice = entry.get().strip()
    if num_dice.isdigit():
        num_dice = int(num_dice)
        die_type = int(die_type_var.get())
        rolls = roll_dice(num_dice, die_type)
        total = sum(rolls)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.INSERT, f"Resultados: {rolls}\n")
        total_label.config(text=f"Total: {total}", fg="gold")
    else:
        result_text.delete("1.0", tk.END)
        result_text.insert(
            tk.INSERT, "Por favor, introduce un numero valido de datos.\n")
        total_label.config(text="")


app = tk.Tk()
app.title("Roll Dice")
app.config(bg="dark slate blue")
app.geometry("600x500")

font_large = ("Arial", 16)  # Fuente mas grande para los resultados y etiquetas
font_extra_large = ("Arial", 20)  # Fuente aun mas grande para el total

entry_label = tk.Label(
    app, text="¿Cuantos dados quieres lanzar?", bg="dark slate blue", fg="white", font=font_large)
entry_label.pack()

entry = tk.Entry(app, font=font_large)
entry.pack()

die_type_label = tk.Label(app, text="Seleccione el tipo de dado:",
                          bg="dark slate blue", fg="white", font=font_large)
die_type_label.pack()

die_type_var = tk.StringVar(app)
die_type_var.set("6")
die_type_options = tk.OptionMenu(
    app, die_type_var, "4", "6", "8", "10", "12", "20", "100")
die_type_options.config(font=font_large)
die_type_options.pack()

roll_button = tk.Button(app, text="Lanzar dados",
                        command=on_roll, bg="black", fg="white", font=font_large)
roll_button.pack()

# Area de texto con desplazamiento para resultados
result_text = scrolledtext.ScrolledText(
    app, width=70, height=10, font=font_large, bg="light grey", fg="black")
result_text.pack()

total_label = tk.Label(app, text="", bg="dark slate blue",
                       fg="gold", font=font_extra_large)
total_label.pack()

app.mainloop()
