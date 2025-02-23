import customtkinter as ctk


class CalculadoraImpuestos:
    def __init__(self):
        self.ventana = ctk.CTk()
        self.ventana.title('Calculadora de Impuestos')
        self.ventana.geometry('350x250')
        self.ventana.resizable(width=False, height=False)

        # Relleno de widgets y tama;o de fuente
        self.padding: dict = {'padx': 20, 'pady': 10}
        self.font = ('Arial', 12)  # Define el tipo y tamaño de la fuente
        self.etiqueta_ingreso = ctk.CTkLabel(
            self.ventana, text='Ingreso: ', font=self.font)
        self.etiqueta_ingreso.grid(row=0, column=0, **self.padding)
        self.entrada_ingreso = ctk.CTkEntry(self.ventana, font=self.font)
        self.entrada_ingreso.grid(row=0, column=1, **self.padding)
        self.etiqueta_porcentaje = ctk.CTkLabel(
            self.ventana, text='Porcentaje: ', font=self.font)
        self.etiqueta_porcentaje.grid(row=1, column=0, **self.padding)
        self.entrada_porcentaje = ctk.CTkEntry(self.ventana, font=self.font)
        self.entrada_porcentaje.grid(row=1, column=1, **self.padding)
        self.etiqueta_resultado = ctk.CTkLabel(
            self.ventana, text='Impuesto: ', font=self.font)
        self.etiqueta_resultado.grid(row=2, column=0, **self.padding)
        self.entrada_resultado = ctk.CTkEntry(self.ventana, font=self.font)
        self.entrada_resultado.insert(0, '0')
        self.entrada_resultado.grid(row=2, column=1, **self.padding)
        self.boton_calcular = ctk.CTkButton(
            self.ventana, text='Calcular', font=self.font, command=self.calcular_impuesto)
        self.boton_calcular.grid(row=3, column=1, **self.padding)

    def actualizar_resultado(self, texto):
        self.entrada_resultado.insert(0, texto)

    def calcular_impuesto(self):
        self.entrada_resultado.delete(0, ctk.END)
        try:
            ingreso: float = float(self.entrada_ingreso.get())
            porcentaje: float = float(self.entrada_porcentaje.get())
            self.actualizar_resultado(f'${ingreso * (porcentaje / 100):,.2f}')
        except ValueError:
            self.actualizar_resultado('Entrada invalida')

    def ejecutar(self):
        # Ejecuta la aplicacion tkinter
        self.ventana.mainloop()


calculadora = CalculadoraImpuestos()
calculadora.ejecutar()
