FROM python:3.10-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo requirements.txt
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir --disable-pip-version-check -r requirements.txt

# Copiar todos los archivos del contexto actual al contenedor
COPY . .

# Exponer el puerto de la aplicación
EXPOSE 8000

# Comando de inicio
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
