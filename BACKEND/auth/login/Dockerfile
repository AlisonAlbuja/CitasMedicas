FROM python:3.10-slim
 
# Set the working directory inside the container
WORKDIR /app
 
# Copy the requirements.txt file
COPY requirements.txt ./

RUN pip install --upgrade pip 

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
 
# Copy all files, including .env
COPY . .
 
# Expose the application port
EXPOSE 8000
 
# Startup command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
