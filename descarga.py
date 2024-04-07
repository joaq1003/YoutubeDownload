import pytube as tube

def descargar_audio(url,ruta_descarga):
    try:
        #Creo un objeto youtube con la URL que me dieron
        video = tube.YouTube(url)

        #Filtro solo el audio para descargar
        stream = video.streams.filter(only_audio=True).first()

        #Descargo
        stream.download(output_path=ruta_descarga)

        print("Descargado Correctamente")
    except Exception as e:
        print("Se produjo un error al descargar el audio",e)

def descargar_video(url,ruta_descarga):
    try:
        #Creo un objeto Youtube con la URL proporcionada
        video = tube.YouTube(url)

        #Seleccionar la mejor calidad para decargar
        stream = video.streams.get_highest_resolution()

        #Descargar el video en la ruta especificada
        stream.download(output_path = ruta_descarga)

        print("Descargado correctamente")

    except Exception as e:
        print("Ocurrio un error al descargar el video",e)

vector_links = ["https://www.youtube.com/watch?v=2pnK914JzHk&list=RD2pnK914JzHk&start_radio=1","https://www.youtube.com/watch?v=viodWcwQnSE"]

#for link in vector_links:
#    descargar_video(link,ruta_descarga="C:\\Users\\Acer\\OneDrive\\Desktop\\Videos Descargados")

#for link in vector_links:
    #descargar_audio(link,ruta_descarga="C:\\Users\\Acer\\OneDrive\\Desktop\\Videos Descargados")