# Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the dependencies file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY . .
RUN rm -f .env  # Remove the .env from the container for security

# Set the necessary environment variables
ENV FLASK_APP=main
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONPATH=/app

# Expose a new port
EXPOSE 8080

# Command to run the application on the new port
CMD ["flask", "run", "--port=8080"]
