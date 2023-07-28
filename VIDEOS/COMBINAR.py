import ffmpeg



input_video = ffmpeg.input("VIDEOS/Undertale_V.mp4")

input_audio = ffmpeg.input("VIDEOS/Undertale_M.webm")


ffmpeg.concat(input_video, input_audio, v=1, a=1).output("VIDEOS/ALMACEN/final.mp4").run()



