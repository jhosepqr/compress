# 🗜️ Compresor de Medios (Audio y Video)

Un script en Python sencillo, eficiente y **portable** para comprimir automáticamente tus archivos de audio y video. 

Este proyecto utiliza `pydub` y `imageio-ffmpeg` para garantizar que no necesites instalar FFmpeg manualmente en tu sistema (configuración de PATH, etc.), haciendo que la herramienta sea completamente *plug-and-play*.

---

## ✨ Características

- 🎵 **Compresión de Audio**: Reduce el tamaño de archivos `.mp3` ajustando el *bitrate* (por defecto a 64k).
- 🎬 **Compresión de Video**: Soporte para formatos `.mp4`, `.mkv` y `.mov`. Utiliza el codec `libx264` para un balance perfecto entre calidad y tamaño de archivo (CRF ajustable).
- 🚀 **Portabilidad (FFmpeg incorporado)**: Gracias a `imageio-ffmpeg`, el ejecutable de FFmpeg se gestiona automáticamente de forma interna. ¡No requiere instalaciones adicionales en el sistema!
- 📂 **Procesamiento por Lotes (Batch)**: Procesa todos los archivos compatibles ubicados en la misma carpeta del script de una sola vez.

---

## 🛠️ Requisitos e Instalación

Asegúrate de tener Python instalado en tu sistema. Luego, instala las dependencias necesarias ejecutando:

```bash
pip install pydub imageio-ffmpeg
```

---

## 🚀 Modo de Uso

1. Coloca el archivo `compress.py` en la misma carpeta donde se encuentran los archivos de audio o video que deseas comprimir.
2. Abre una terminal o línea de comandos en esa misma ruta.
3. Ejecuta el script:

```bash
python compress.py
```

4. El script mostrará un menú interactivo:
   - Presiona `1` para comprimir archivos de **Audio**.
   - Presiona `2` para comprimir archivos de **Video**.
5. Los archivos resultantes se guardarán automáticamente dentro de una nueva subcarpeta llamada `comprimidos`, añadiendo el prefijo `compressed_` al nombre original.

---

## ⚙️ Detalles Técnicos y Configuración

Si deseas ajustar los niveles de compresión, puedes modificar los siguientes parámetros dentro de la función `compress_media` en el código fuente:

- **Audio (`target_audio_bitrate`)**: Configurado por defecto a `"64k"`. Puedes cambiarlo a `"128k"`, `"96k"`, etc., según la calidad que desees conservar.
- **Video (`video_crf`)**: Configurado por defecto a `28`. El *Constant Rate Factor* (CRF) controla la calidad. Un valor menor significa mejor calidad y mayor tamaño; un valor mayor significa menor tamaño y menor calidad (los valores entre 24 y 30 son ideales para compresión). El parámetro `-preset fast` se encarga de optimizar la velocidad del proceso.

---

## 💡 ¿Por qué es portable?

El mayor dolor de cabeza al trabajar con procesamiento multimedia en Python suele ser la instalación manual de FFmpeg. Este proyecto resuelve ese problema importando `imageio_ffmpeg`, el cual provee un binario de FFmpeg local al entorno virtual. Este binario es configurado directamente en `pydub` (`AudioSegment.converter = ffmpeg_path`) y utilizado en las llamadas a `subprocess` para procesar video de forma independiente.
