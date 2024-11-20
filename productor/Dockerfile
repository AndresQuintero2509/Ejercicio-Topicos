# 1. Especifica una imagen base
FROM python:3.9-slim

# 2. Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copia los archivos necesarios al contenedor
COPY requirements.txt ./
COPY app.py ./

# 4. Instala las dependencias especificadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. Expone un puerto (opcional, si la app es un servidor)
EXPOSE 5050

# 6. Especifica el comando por defecto al iniciar el contenedor
CMD ["python", "app.py"]