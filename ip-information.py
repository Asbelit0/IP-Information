import tkinter as tk
from tkinter import ttk
import requests

class Aplicacion:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Buscar información de una dirección IP")
        self.raiz.geometry("520x300")
        self.raiz.configure(bg="grey")

        # Crear etiquetas y campos de texto
        self.etiqueta_direccion_ip = ttk.Label(self.raiz, text="Dirección IP:")
        self.etiqueta_direccion_ip.grid(column=0, row=0, padx=5, pady=20)

        self.campo_direccion_ip = ttk.Entry(self.raiz, width=50)
        self.campo_direccion_ip.grid(column=1, row=0, padx=5, pady=5)

        self.etiqueta_resultado = ttk.Label(self.raiz, text="Resultado:")
        self.etiqueta_resultado.grid(column=0, row=1, padx=5, pady=5)

        self.campo_resultado = tk.Text(self.raiz, width=50, height=10)
        self.campo_resultado.grid(column=1, row=1, padx=5, pady=5)

        # Crear botón para buscar información
        self.boton_buscar = ttk.Button(self.raiz, text="Buscar", command=self.buscar_informacion)
        self.boton_buscar.grid(column=1, row=2, padx=5, pady=25)

    def buscar_informacion(self):
        direccion_ip = self.campo_direccion_ip.get()
        if direccion_ip:
            url = f"http://ip-api.com/json/{direccion_ip}"
            respuesta = requests.get(url)
            if respuesta.status_code == 200:
                datos = respuesta.json()
                self.campo_resultado.delete(1.0, tk.END)
                self.campo_resultado.insert(tk.END, f"País: {datos['country']}\n")
                self.campo_resultado.insert(tk.END, f"Región: {datos['region']}\n")
                self.campo_resultado.insert(tk.END, f"Ciudad: {datos['city']}\n")
                self.campo_resultado.insert(tk.END, f"Coordenadas: {datos['lat']}, {datos['lon']}\n")
                self.campo_resultado.insert(tk.END, f"Organización: {datos['org']}\n")
                self.campo_resultado.insert(tk.END, f"Proveedor: {datos['isp']}\n")
            else:
                self.campo_resultado.delete(1.0, tk.END)
                self.campo_resultado.insert(tk.END, "Error al buscar información")
        else:
            self.campo_resultado.delete(1.0, tk.END)
            self.campo_resultado.insert(tk.END, "Por favor, ingrese una dirección IP")

if __name__ == "__main__":
    raiz = tk.Tk()
    aplicacion = Aplicacion(raiz)
    raiz.mainloop()