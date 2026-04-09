import os
import subprocess
import imageio_ffmpeg
from pydub import AudioSegment

# Obtener la ruta del ejecutable de ffmpeg
ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()

# Configurar pydub para usar el ffmpeg que se descargó por imageio-ffmpeg
AudioSegment.converter = ffmpeg_path

def compress_media(input_folder, output_folder, mode, target_audio_bitrate="64k", video_crf=28):
    """
    Comprime archivos de audio (MP3) o video (MP4, MKV, MOV) según la opción seleccionada.
    - video_crf: Controla la calidad del video (0-51). 
                 Menor = mejor calidad. Mayor = menor tamaño (24 a 30 es buen balance para compresión).
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    archivos_procesados = False

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"compressed_{filename}")

        # Procesar audio MP3 (Modo 1)
        if mode == "1" and filename.lower().endswith(".mp3"):
            archivos_procesados = True
            print(f"Comprimiendo AUDIO {filename} a {target_audio_bitrate}...")
            try:
                # Cargar el archivo de audio
                audio = AudioSegment.from_mp3(input_path)
                # Exportar con el nuevo bitrate
                audio.export(output_path, format="mp3", bitrate=target_audio_bitrate)
                print(f"Guardado exitosamente: {output_path}")
            except Exception as e:
                print(f"Error al procesar audio {filename}: {e}")

        # Procesar videos (Modo 2)
        elif mode == "2" and filename.lower().endswith((".mp4", ".mov", ".mkv")):
            archivos_procesados = True
            print(f"Comprimiendo VIDEO {filename} (CRF {video_crf}). Esto puede demorar...")
            try:
                # Comando FFmpeg para comprimir video en H.264
                command = [
                    ffmpeg_path,
                    "-y",                 # Sobrescribir archivo si existe
                    "-i", input_path,     # Archivo de entrada
                    "-vcodec", "libx264", # Codec de video estándar y eficiente
                    "-crf", str(video_crf), # Factor de compresión
                    "-preset", "fast",    # Velocidad de compresión (fast/medium/slow)
                    "-acodec", "aac",     # Codec de audio para video
                    output_path           # Archivo de salida
                ]
                
                # Ejecutar comando llamando a ffmpeg y suprimiendo la salida extendida
                subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print(f"Guardado exitosamente: {output_path}")
            except Exception as e:
                print(f"Error al procesar video {filename}: {e}")

    if not archivos_procesados:
        print("No se encontraron archivos compatibles para la opción seleccionada en la carpeta actual.")

if __name__ == "__main__":
    # Carpeta actual
    current_folder = os.getcwd()
    # Carpeta donde se guardarán los archivos comprimidos
    output_folder = os.path.join(current_folder, "comprimidos")
    
    print("========================================")
    print(" COMPRESOR DE MEDIOS (Audio y Video)")
    print("========================================")
    print("¿Qué deseas comprimir?")
    print("1. Audio (Archivos MP3)")
    print("2. Video (Archivos MP4, MKV, MOV)")
    print("========================================")
    
    opcion = input("Elige una opción (1 o 2): ").strip()
    
    if opcion in ["1", "2"]:
        print(f"\nIniciando proceso...")
        compress_media(current_folder, output_folder, mode=opcion, target_audio_bitrate="64k", video_crf=28)
        print("\n¡Proceso terminado!")
    else:
        print("Opción no válida. Debes ingresar '1' o '2'.")
