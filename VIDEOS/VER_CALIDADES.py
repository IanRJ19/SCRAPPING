from pytube import YouTube

link = "https://www.youtube.com/watch?v=qWvbOmT7rTw"
yt = YouTube(link)

# se muestra informacion del video
print("Su video es:")
print("\tTitulo:", yt.title)
print("\tAutor:", yt.author)

duracion = yt.length  # seg
horas = int(duracion/60/60)
duracion -= horas*60*60
minutos = int((duracion)/60)
duracion -= minutos*60
segundos = int(duracion)

print("\tDuracion:", f"{horas}:{minutos}:{segundos}")

# mostrar todas las opciones de calidad disponibles
print("Opciones de calidad disponibles para descargar:")
streams = yt.streams
for e in streams:
    print(e)
# aqui puedes seleccionar una opción específica para descargar
# por ejemplo, para descargar la primera opción:
# primera_opcion = streams[0]
# primera_opcion.download(output_path="VIDEOS/ALMACEN")

print("Termino, adios!")
