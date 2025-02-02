# Usar Python 3.9 como base
FROM python:3.9

# Definir el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo requirements.txt primero (para aprovechar la caché de Docker)
COPY requirements.txt /app/

# Instalar dependencias, incluyendo pymysql
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copiar el código de la aplicación al contenedor
COPY . /app/

# Comando para ejecutar el microservicio
CMD ["uvicorn", "app.routers.main:app", "--host", "0.0.0.0", "--port", "8001"]
