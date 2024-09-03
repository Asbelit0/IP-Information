import tkinter as tk
from tkinter import ttk
import requests

class Aplication:
    BACKGROUND_COLOR = "white"
    FONT = ("Arial", 12, "italic", "bold")

    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Buscar información de una dirección IP")
        self.raiz.geometry("550x300")
        self.raiz.configure(bg=self.BACKGROUND_COLOR)

        self.create_widgets()

    def create_widgets(self):
        #Etiquetas y campos de texto
        self.label_ip_address = ttk.Label(self.raiz, text="Dirección IP:", background=self.BACKGROUND_COLOR, 
                                        font=self.FONT)
        self.label_ip_address.grid(column=0, row=0, padx=5, pady=20)

        self.campo_direccion_ip = ttk.Entry(self.raiz, width=30, background=self.BACKGROUND_COLOR, 
                                            font=self.FONT)
        self.campo_direccion_ip.grid(column=1, row=0, padx=5, pady=5)
        self.campo_direccion_ip.config(justify="center")

        self.label_resultado = ttk.Label(self.raiz, text="Resultado:", background=self.BACKGROUND_COLOR, 
                                        font=self.FONT)
        self.label_resultado.grid(column=0, row=1, padx=5, pady=5)

        self.camp_result = tk.Text(self.raiz, width=50, height=10, borderwidth=2, relief="groove")
        self.camp_result.grid(column=1, row=1, padx=5, pady=5)

        #Botón para buscar información
        self.boton_buscar = ttk.Button(self.raiz, text="Buscar", command=self.search_information)
        self.boton_buscar.grid(column=1, row=2, padx=5, pady=25)

        #Evento boton buscar
        self.campo_direccion_ip.bind("<Return>", lambda event: self.search_information())

    def search_information(self):
        try:
            direccion_ip = self.campo_direccion_ip.get()
            if direccion_ip:
                url = f"http://ip-api.com/json/{direccion_ip}"
                respuesta = requests.get(url)
                if respuesta.status_code == 200:
                    datos = respuesta.json()
                    self.show_result(datos)
                else:
                    self.show_error("Error al buscar información")
            else:
                self.show_error("Por favor, ingrese una dirección IP")
        except ValueError:
            self.show_error("No es una dirección IP válida")

    def show_result(self, datos):
        self.camp_result.delete(1.0, tk.END)
        self.camp_result.insert(tk.END, f"País: {datos['country']}\n")
        self.camp_result.insert(tk.END, f"Región: {datos['region']}\n")
        self.camp_result.insert(tk.END, f"Ciudad: {datos['city']}\n")
        self.camp_result.insert(tk.END, f"Coordenadas: {datos['lat']}, {datos['lon']}\n")
        self.camp_result.insert(tk.END, f"Organización: {datos['org']}\n")
        self.camp_result.insert(tk.END, f"Proveedor: {datos['isp']}\n")

    def show_error(self, mensaje):
        self.camp_result.delete(1.0, tk.END)
        self.camp_result.insert(tk.END, mensaje)

if __name__ == "__main__":
    raiz = tk.Tk()
    aplication = Aplication(raiz)
    raiz.mainloop()