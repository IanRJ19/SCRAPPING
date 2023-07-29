from pytube import YouTube
import ffmpeg
import os

# La lista de enlaces
links = ["https://www.youtube.com/watch?v=AwmvwTopbas",
         "https://www.youtube.com/watch?v=Zf9U1O7qFWc",
         "https://www.youtube.com/watch?v=JdDJRhBuypU",
         "https://www.youtube.com/watch?v=bxLMqst4ut4"]

# Itera a través de cada enlace en la lista
for link in links:
    yt = YouTube(link)

    print("Su video es:")
    print("\tTitulo:", yt.title)
    print("\tAutor:", yt.author)

    duracion = yt.length
    horas = int(duracion/60/60)
    duracion -= horas*60*60
    minutos = int((duracion)/60)
    duracion -= minutos*60
    segundos = int(duracion)

    print("\tDuracion:", f"{horas}:{minutos}:{segundos}")

    print("Descargando")

    print("\t", yt.streams.filter(only_video=True).order_by("resolution").desc().first())
    print("\t", yt.streams.filter(only_audio=True).order_by("abr").desc().first())

    video_stream = yt.streams.filter(only_video=True).order_by('resolution').desc().first()
    audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()

    # Create a list of allowed characters
    allowed_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_ ")

    # Clean the video title
    filename = "".join(c if c in allowed_chars else "_" for c in yt.title)

    video_filename = f"{filename}_video"
    audio_filename = f"{filename}_audio"
    output_filename = f"{filename}_MIX"

    video_stream.download(output_path="VIDEOS/ALMACEN", filename=video_filename)
    audio_stream.download(output_path="VIDEOS/ALMACEN", filename=audio_filename)

    input_video = ffmpeg.input(f'VIDEOS/ALMACEN/{video_filename}')
    input_audio = ffmpeg.input(f'VIDEOS/ALMACEN/{audio_filename}')

    ffmpeg.output(input_video, input_audio, f'VIDEOS/ALMACEN/{output_filename}.mkv', c='copy').run()

    # Removing the intermediate files
    os.remove(f'VIDEOS/ALMACEN/{video_filename}')
    os.remove(f'VIDEOS/ALMACEN/{audio_filename}')

    print("Termino, adios!")
