import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import os

#Creamos la ventana principal:
ventana = tk.Tk()
ventana.title("Calculadora basica")
ventana.geometry("600x300")


try: 
    #Crear una imagen de fondo
    imagen = Image.open(os.path.join("calculator_image", "guts.png")).convert("RGBA")
    blanco = Image.new('RGBA', imagen.size, (255, 255, 255, 255))
    imagen = Image.blend(imagen, blanco, 0.85)
    imagen = imagen.resize((600, 300), Image.LANCZOS)
    imagen = ImageTk.PhotoImage(imagen)
    imagen_label = tk.Label(ventana, image=imagen)
    imagen_label.place(x=0,y=0, relwidth=1, relheight=1)
except FileNotFoundError:
    messagebox.showwarning("Error", "No se encontró la imagen 'guts.png'. Usando fondo predeterminado.")



#Crear dos ventanas de numeradores:
numero1 = tk.Entry(ventana, width=15)
numero1.pack(pady=10)
numero2 = tk.Entry(ventana, width=15)
numero2.pack(pady=10)

val_final = tk.Label(ventana, text="Aqui se mostrara el resultado final del calculo.")
val_final.pack(pady=10)

#Funcion sumar:
def sumar():
    try:
        N1 = float(numero1.get())
        N2 = float(numero2.get())
        res = N1 + N2
        val_final.config(text=str(res))
    except ValueError:
        messagebox.showerror("Alerta", "Escribe un valor numerico valido rapa tu madre")

#Funcion restar:
def restar():
    try:
        N1 = float(numero1.get())
        N2 = float(numero2.get())
        res = N1 - N2
        val_final.config(text=str(res))
    except ValueError:
        messagebox.showerror("Alerta", "Escribe un valor numerico valido rapa tu madre")

def multi():
    try:
        N1 = float(numero1.get())
        N2 = float(numero2.get())
        res = N1 * N2
        val_final.config(text=str(res))
    except ValueError:
        messagebox.showerror("Alerta", "Escribe un valor numerico valido rapa tu madre")

def div():
    try:
        N1 = float(numero1.get())
        N2 = float(numero2.get())
        res = N1 / N2
        val_final.config(text=str(res))
    except ValueError:
        messagebox.showerror("Alerta", "Escribe un valor numerico valido rapa tu madre")

#Crar un frame para colocar bien los botones:
frame_boton = tk.Frame(ventana)  
frame_boton.pack(pady=10)

# Crear un botón que sume:
boton = tk.Button(frame_boton, text="Sumar", command=sumar)
boton.pack(side=tk.LEFT, padx=5)

#Crear un boton que reste:
boton1 = tk.Button(frame_boton, text="Restar", command=restar)
boton1.pack(side=tk.LEFT, padx=5)

#Crear un boton que multiplique:
boton2 = tk.Button(frame_boton, text="Multiplicar", command=multi)
boton2.pack(side=tk.LEFT, padx=5)

#Crear un boton que divide:
boton3 = tk.Button(frame_boton, text="Dividir", command=div)
boton3.pack(side=tk.LEFT,padx=5)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
