# Usar Python 3.9 como base
FROM python:3.9

# Definir el directorio de trabajo dentro del contenedor
WORKDIR /appDefine the working directory within the container

# Copiar el archivo requirements.txt primero (para aprovechar la caché de Docker)
COPY requirements.txt /app/

# Actualizar pip antes de instalar dependencias
RUN pip install --upgrade pip 

# Instalar todas las dependencias excepto mysql-connector-python
RUN pip install --no-cache-dir fastapi==0.95.2 pydantic==1.10.2 python-dotenv==0.21.0 uvicorn==0.22.0 pymysql requests PyJWT==2.6.0

# Instalar mysql-connector-python por separado (para evitar timeout)
RUN pip install --no-cache-dir mysql-connector-python==8.0.32

# Copiar el código de la aplicación al contenedor
COPY . /app/

# Comando para ejecutar el microservicio
CMD ["uvicorn", "app.routers.main:app", "--host", "0.0.0.0", "--port", "8001"]
