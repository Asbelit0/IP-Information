import tkinter as tk
from tkinter import ttk
import requests

class Aplicacion:
    COLOR_FONDO = "grey"
    FUENTE = ("Arial", 12, "italic", "bold")

    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Buscar información de una dirección IP")
        self.raiz.geometry("550x300")
        self.raiz.configure(bg=self.COLOR_FONDO)

        self.crear_widgets()

    def crear_widgets(self):
        #Etiquetas y campos de texto
        self.label_ip_address = ttk.Label(self.raiz, text="Dirección IP:", background=self.COLOR_FONDO, 
                                        font=self.FUENTE)
        self.label_ip_address.grid(column=0, row=0, padx=5, pady=20)

        self.campo_direccion_ip = ttk.Entry(self.raiz, width=30, background=self.COLOR_FONDO, 
                                            font=self.FUENTE)
        self.campo_direccion_ip.grid(column=1, row=0, padx=5, pady=5)
        self.campo_direccion_ip.config(justify="center")

        self.label_resultado = ttk.Label(self.raiz, text="Resultado:", background=self.COLOR_FONDO, 
                                        font=self.FUENTE)
        self.label_resultado.grid(column=0, row=1, padx=5, pady=5)

        self.campo_resultado = tk.Text(self.raiz, width=50, height=10, borderwidth=2, relief="groove")
        self.campo_resultado.grid(column=1, row=1, padx=5, pady=5)

        #Botón para buscar información
        self.boton_buscar = ttk.Button(self.raiz, text="Buscar", command=self.buscar_informacion)
        self.boton_buscar.grid(column=1, row=2, padx=5, pady=25)

        #Evento boton buscar
        self.campo_direccion_ip.bind("<Return>", lambda event: self.buscar_informacion())

    def buscar_informacion(self):
        direccion_ip = self.campo_direccion_ip.get()
        if direccion_ip:
            url = f"http://ip-api.com/json/{direccion_ip}"
            respuesta = requests.get(url)
            if respuesta.status_code == 200:
                datos = respuesta.json()
                self.mostrar_resultado(datos)
            else:
                self.mostrar_error("Error al buscar información")
        else:
            self.mostrar_error("Por favor, ingrese una dirección IP")

    def mostrar_resultado(self, datos):
        self.campo_resultado.delete(1.0, tk.END)
        self.campo_resultado.insert(tk.END, f"País: {datos['country']}\n")
        self.campo_resultado.insert(tk.END, f"Región: {datos['region']}\n")
        self.campo_resultado.insert(tk.END, f"Ciudad: {datos['city']}\n")
        self.campo_resultado.insert(tk.END, f"Coordenadas: {datos['lat']}, {datos['lon']}\n")
        self.campo_resultado.insert(tk.END, f"Organización: {datos['org']}\n")
        self.campo_resultado.insert(tk.END, f"Proveedor: {datos['isp']}\n")

    def mostrar_error(self, mensaje):
        self.campo_resultado.delete(1.0, tk.END)
        self.campo_resultado.insert(tk.END, mensaje)

if __name__ == "__main__":
    raiz = tk.Tk()
    aplicacion = Aplicacion(raiz)
    raiz.mainloop()