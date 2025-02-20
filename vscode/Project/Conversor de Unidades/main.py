import tkinter as tk


def convertir_a_fahrenheit():
    celsius = float(celsius_entry.get())
    fahrenheit = round(celsius * 9 / 5 + 32, 1)
    result_label.config(text=f"{fahrenheit} Fahrenheit")


def convertir_a_celsius():
    fahrenheit = float(fahrenheit_entry.get())
    celsius = round((fahrenheit - 32) * 5 / 9, 1)
    result_label.config(text=f"{celsius} Celsius")


app = tk.Tk()
app.title("Convertidor de Temperatura")
app.geometry("400x300")
app.configure(bg="light blue")

label_font = ("Verdana", 10, "bold")
entry_font = ("Verdana", 10)
button_font = ("Verdana", 10, "bold")

tk.Label(app, text="Celsius a Fahrenheit: ",
         font=label_font, bg="light blue").pack(pady=5)

celsius_entry = tk.Entry(app, font=entry_font)
celsius_entry.pack(pady=5)
tk.Button(app, text="Convertir a Fahrenheit", font=button_font,
          command=convertir_a_fahrenheit, bg="light gray").pack(pady=5)

tk.Label(app, text="Fahrenheit a Celsius: ",
         font=label_font, bg="light blue").pack(pady=5)

fahrenheit_entry = tk.Entry(app, font=entry_font)
fahrenheit_entry.pack(pady=5)
tk.Button(app, text="Convertir a Celsius", font=button_font,
          command=convertir_a_celsius, bg="light gray").pack(pady=5)

result_label = tk.Label(app, text="Resultado",
                        font=label_font, bg="light blue")
result_label.pack(pady=10)

app.mainloop()
