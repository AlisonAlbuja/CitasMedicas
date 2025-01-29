FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --disable-pip-version-check -r requirements.txt

# Copy all files from the current context to the container
COPY . .
RUN rm -f .env  # Remove the .env file from the container for security

# Expose the application port
EXPOSE 8000

# Startup command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
