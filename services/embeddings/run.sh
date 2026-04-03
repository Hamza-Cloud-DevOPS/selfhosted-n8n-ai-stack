#!/bin/bash

# Script para levantar LocalAI con embeddings
# Crea la carpeta de modelos si no existe y arranca el servicio

# Crear la carpeta de modelos si no existe
mkdir -p ./models

# Ir a la carpeta donde está el docker-compose
cd "$(dirname "$0")"

# Construir y levantar en segundo plano
docker-compose up -d --build

echo "✅ LocalAI levantado en http://localhost:8081/v1/embeddings"
echo "📦 Modelo: all-MiniLM-L6-v2"
