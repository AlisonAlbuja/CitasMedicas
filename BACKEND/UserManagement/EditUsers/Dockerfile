# Imagen base de Python
FROM python:3.9

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de dependencias
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente al contenedor
COPY . .

# Establecer las variables de entorno necesarias
ENV FLASK_APP=main
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONPATH=/app

# Exponer un nuevo puerto
EXPOSE 8080

# Comando para ejecutar la aplicación en el nuevo puerto
CMD ["flask", "run", "--port=8080"]
