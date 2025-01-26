FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar y instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente al contenedor
COPY . .

# Exponer el puerto
EXPOSE 5000

# Comando para iniciar el microservicio
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
