import tkinter as tk
from tkinter import ttk
import requests

class Aplicacion:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Buscar información de una dirección IP")
        self.raiz.geometry("520x300")
        self.raiz.configure(bg="grey")

