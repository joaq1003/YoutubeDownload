import descarga as desc
import tkinter as tk
from tkinter import messagebox
import numpy as np
from tkinter import ttk

links = [] #Vector en donde pongo los links

def agregar_link():
    link = cuadro_texto.get()
    if link != "":
        links.append(link)
        cuadro_texto.delete(0,tk.END) #Borro el contenido del cuadro de texto

def descargar():
    selection = opcion_seleccionada.get()
    cantidad_links = np.size(links)
    if cantidad_links != 0:
        answer = messagebox.askyesno("Confirmacion", f"Estas por descargar {cantidad_links} videos")
        if answer:
            if selection == "Audios":
                for posicion,link in enumerate(links):
                    mensaje = f"Video numero {posicion + 1} de {cantidad_links}"

        if selection == "Videos":
            for link in links:
                desc.descargar_video(link,"C:\\Users\\Acer\\OneDrive\\Desktop\\Videos Descargados")

#Funcion para salir del programa
def salir():
    ventana.quit()

#Funcion para limpiar lista de descarga
def limpiar():
    links.clear()

# Definir la ventana
ventana = tk.Tk()
ventana.title("Descargas")

# Obtener las dimensiones de la pantalla
ancho_ventana = 400
alto_ventana = 300
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Calcular la posición para centrar la ventana en la pantalla
x = (ancho_pantalla // 2) - (ancho_ventana // 2)
y = (alto_pantalla // 2) - (alto_ventana // 2)

# Concatenar las dimensiones y la posición para establecer la geometría de la ventana
geometry_string = f"{ancho_ventana}x{alto_ventana}+{x}+{y}"
ventana.geometry(geometry_string)

# Label
label = tk.Label(ventana, text="Ingresa el link:")
label.pack(padx=5, pady=5)

# Cuadro de texto en donde ponemos el link
cuadro_texto = tk.Entry(ventana, width=ancho_ventana - 10)
cuadro_texto.pack(side = tk.TOP,padx=5, pady=5)

# Botón para acumular en un vector los links
boton_agregar_link = tk.Button(ventana, text="Agregar link", command=agregar_link)
boton_agregar_link.pack(side=tk.LEFT, padx=5, pady=5)

# Botón para descargar
boton_descarga = tk.Button(ventana, text="Descargar", command = descargar)
boton_descarga.pack(side=tk.LEFT, padx=5, pady=5)

#Boton para limpiar lista de descarga
boton_limpiar = tk.Button(ventana,text = "Limpiar",command = limpiar)
boton_limpiar.pack(side=tk.LEFT,padx = 5, pady = 5)

# Botón para salir
boton_salir = tk.Button(ventana, text="Salir", command=salir)
boton_salir.pack(side=tk.LEFT,padx=5, pady=5)

# Variable para almacenar la opción seleccionada
opcion_seleccionada = tk.StringVar()

# Opciones para que podamos elegir
options_videos = tk.Radiobutton(ventana, text="Descargar Videos", variable=opcion_seleccionada, value="Videos")
options_videos.pack(side=tk.TOP, padx=10, pady=5)

options_audios = tk.Radiobutton(ventana, text="Descargar Audios", variable=opcion_seleccionada, value="Audios")
options_audios.pack(side=tk.TOP, padx=10, pady=5)

# Ejecutar el bucle de eventos
ventana.mainloop()