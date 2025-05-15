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
    tk.Label(ventana, text="Escoja su opción", font=("Arial", 12, "bold")).pack(pady=10)

    # Botones para las opciones
    tk.Button(ventana, text="Longitud", command=ventana_longitud, width=20, height=2, bg="#fb8c00", fg="white").pack(pady=5)
    tk.Button(ventana, text="Masa", command=ventana_masa, width=20, height=2, bg="#fb8c00", fg="white" ).pack(pady=5)
    tk.Button(ventana, text="Tiempo", command=ventana_tiempo, width=20, height=2, bg="#fb8c00", fg="white" ).pack(pady=5)

    ventana.mainloop()

#Ventana de conversión longitud
def ventana_longitud():
    ventana = tk.Tk()
    ventana.title("Longitud")
    ventana.geometry("300x250")
    ventana.configure(bg="white")

    tk.Label(ventana, text="Seleccione tipo de conversión: ").pack()
    combo =ttk.Combobox(ventana, values= ["Metros --> Kilómetros", "Pulgadas --> Metros"])
    combo.pack()

    tk.Label(ventana, text="Ingrese valor: ").pack()
    entrada = tk.Entry(ventana)
    entrada.pack()

    resultado = tk.Label(ventana, text="Resultado: ")
    resultado.pack()

    def conversion(): #Fórmula de la conversión dependiendo del tipo
        valor = float(entrada.get())
        seleccion = combo.get()
        if seleccion == "Metros --> Kilómetros":
            res_longitud = round(valor / 1000, 3)
            resultado.config(text=f"Resultado: {res_longitud} km")
        elif seleccion == "Pulgadas --> Metros":
            res_longitud = round(valor / 39.37, 3)
            resultado.config(text=f"Resultado: {res_longitud} m")
        else:
            resultado.config(text="Seleccione una conversión válida")

    tk.Button(ventana, text="Convertir", command=conversion).pack()

#Ventana conversión de masa
def ventana_masa():
    ventana = tk.Tk()
    ventana.title("Masa")
    ventana.geometry("300x250")
    ventana.configure(bg="white")

    tk.Label(ventana, text="Seleccione tipo de conversión:").pack()
    combo = ttk.Combobox(ventana, values=["Kilogramos --> Gramos", "Libras --> Kilogramos"])
    combo.pack()

    tk.Label(ventana, text="Ingrese valor:").pack()
    entrada = tk.Entry(ventana)
    entrada.pack()

    resultado = tk.Label(ventana, text="Resultado: ")
    resultado.pack()

    def conversion(): 
        valor = float(entrada.get())
        seleccion = combo.get()
        if seleccion == "Kilogramos --> Gramos":
            res_masa = round(valor * 1000, 3)
            resultado.config(text=f"Resultado: {res_masa} gr")
        elif seleccion == "Libras --> Kilogramos":
            res_masa = round(valor / 2.205, 3)
            resultado.config(text=f"Resultado: {res_masa} kg")
        else:
            resultado.config(text="Seleccione una conversión válida")

    tk.Button(ventana, text="Convertir", command=conversion).pack()

# Ventana para conversión de tiempo
def ventana_tiempo():
    ventana = tk.Tk()
    ventana.title("Tiempo")
    ventana.geometry("300x250")
    ventana.configure(bg="white")

    tk.Label(ventana, text="Seleccione tipo de conversión:").pack()
    combo = ttk.Combobox(ventana, values=["Segundos --> Minutos", "Horas --> Días"])
    combo.pack()

    tk.Label(ventana, text="Ingrese valor:").pack()
    entrada = tk.Entry(ventana)
    entrada.pack()

    resultado = tk.Label(ventana, text="Resultado: ")
    resultado.pack()

    def conversion(): 
        valor = float(entrada.get())
        seleccion = combo.get()
        if seleccion == "Segundos --> Minutos":
            res_tiempo = round(valor / 60, 3)
            resultado.config(text=f"Resultado: {res_tiempo} minutos")
        elif seleccion == "Horas --> Días":
            res_tiempo = round(valor / 24, 3)
            resultado.config(text=f"Resultado: {res_tiempo} días")
        else:
            resultado.config(text="Seleccione una conversión válida")

    tk.Button(ventana, text="Convertir", command=conversion).pack()

mostrar_selector()