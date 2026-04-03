# Dockerfile para LocalAI (Embeddings)
# Repo: https://github.com/mudler/LocalAI (MIT License)
# Modelo usado: all-MiniLM-L6-v2 (ideal para hardware limitado)

FROM quay.io/go-skynet/local-ai:latest

# Crear carpeta de modelos en el contenedor
RUN mkdir -p /models

# Directorio de trabajo
WORKDIR /models

# Exponer el puerto de la API
EXPOSE 8080
