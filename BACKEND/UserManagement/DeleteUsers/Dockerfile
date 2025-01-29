FROM python:3.9-slim 

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only necessary files, EXCLUDING .env and sensitive files
COPY . .
RUN rm -f .env  # Remove .env from the container for security

# Expose the port
EXPOSE 5000

# Command to start the microservice
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
