import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Ventana principal con los botones de las categorías
def mostrar_selector():  
    ventana = tk.Tk()
    ventana.title("Conversor")
    ventana.geometry("300x250")
    ventana.configure(bg="#e0f7fa")

    # Etiqueta principal
    tk.Label(ventana, text="Escoja su opción", bg="#a5d6a7", font=("Arial", 12, "bold")).pack(pady=10)

    # Botones para las opciones
    tk.Button(ventana, text="Longitud", width=20, height=2, bg="#fb8c00", fg="white", command=ventana_longitud).pack(pady=5)
    tk.Button(ventana, text="Masa", width=20, height=2, bg="#fb8c00", fg="white", command=ventana_masa).pack(pady=5)
    tk.Button(ventana, text="Tiempo", width=20, height=2, bg="#fb8c00", fg="white", command=ventana_tiempo).pack(pady=5)

#Ventana de conversión
def crear_ventanta_conversion():
    

    