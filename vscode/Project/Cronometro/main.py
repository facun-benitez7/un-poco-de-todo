import tkinter as tk


class Cronometro:
    def __init__(self, master):
        self.master = master
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        self.milisegundos = 0
        self.corriendo = False
        self.display = tk.StringVar()
        self.actualizar_display("00:00:00.000")

        # Configuracion de la interfaz grafica
        self.master.title("Cronometro")
        self.master.configure(bg="#34495e")
        self.master.geometry("300x200")
        self.display_label = tk.Label(master, textvariable=self.display, font=(
            "Arial", 36), bg="#34495e", fg="#ffffff")
        self.display_label.pack()
        self.button_frame = tk.Frame(master, bg="#14495e")
        self.button_frame.pack()

        self.start_button = tk.Button(
            self.button_frame, text="Iniciar", command=self.iniciar, bg="#2ecc71", fg="#ffffff")
        self.start_button.pack(side=tk.LEFT, padx=5, pady=10)

        self.stop_button = tk.Button(
            self.button_frame, text="Pausar", command=self.detener, bg="#e74c3c", fg="#ffffff")
        self.stop_button.pack(side=tk.LEFT, padx=5, pady=10)

        self.reset_button = tk.Button(
            self.button_frame, text="reiniciar", command=self.reiniciar, bg="#3498db", fg="#ffffff")
        self.reset_button.pack(side=tk.RIGHT, padx=5, pady=10)

    # actualizar display
    def actualizar_display(self, tiempo):
        self.display.set(tiempo)

    # Iniciar
    def iniciar(self):
        if not self.corriendo:
            self.corriendo = True
            self.actualizar_cronometro()

    # Detener
    def detener(self):
        self.corriendo = False

    # Reiniciar
    def reiniciar(self):
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        self.milisegundos = 0
        self.actualizar_display("00:00:00.000")

    def actualizar_cronometro(self):
        if self.corriendo:
            self.milisegundos += 10
            if self.milisegundos >= 1000:
                self.milisegundos = 0
                self.segundos += 1
            if self.segundos == 60:
                self.segundos = 0
                self.minutos += 1
            if self.minutos == 60:
                self.minutos = 0
                self.horas += 1

            tiempo_formateado = f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}.{self.milisegundos:03}"
            self.actualizar_display(tiempo_formateado)
            self.master.after(10, self.actualizar_cronometro)


if __name__ == "__main__":
    root = tk.Tk()
    cronometro = Cronometro(root)
    root.mainloop()
