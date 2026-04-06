# Dockerfile para Whisper API
# Basado en: https://github.com/jaypetersdotdev/local-whisper
# Motor: https://github.com/openai/whisper (MIT License)

# Imagen base Python
FROM python:3.10-slim

# Instalar ffmpeg (necesario para whisper) y git (necesario para pip install desde git)
RUN apt-get update && \
    apt-get install -y ffmpeg git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Directorio de trabajo
WORKDIR /app

# Instalar whisper desde el repo oficial de OpenAI
RUN pip install --upgrade pip
RUN pip install git+https://github.com/openai/whisper.git

# Limpiar cache de modelos corruptos
RUN rm -rf /root/.cache/whisper

# Pre-descargar el modelo 'small' para evitar descarga en runtime
# Modelos disponibles: tiny, base, small, medium, large, turbo
# tiny (~1GB VRAM) | base (~1GB) | small (~2GB) | medium (~5GB) | large (~10GB)
# PARA CAMBIAR EL MODELO: Modifica "small" por el modelo de arriba que desees
RUN whisper --model small --help || true

# Exponer puerto de la API
EXPOSE 5001

# Copiar el servidor API y ejecutar
COPY api_server.py /app/api_server.py
ENTRYPOINT ["python", "api_server.py"]
