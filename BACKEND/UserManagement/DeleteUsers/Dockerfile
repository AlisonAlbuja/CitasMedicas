FROM python:3.9-slim 

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar y instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar solo archivos necesarios, EXCLUYENDO .env y archivos sensibles
COPY . .
RUN rm -f .env  # Eliminar el .env del contenedor por seguridad

# Exponer el puerto
EXPOSE 5000

# Comando para iniciar el microservicio
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
