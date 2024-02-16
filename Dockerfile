# Use the official Python Docker image as a base
FROM python:3.10-slim

# Set environment variable for the service account key file path
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/gcp-service-account.json

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Create and set the working directory
WORKDIR /app

# Copy the service account key file into the container
COPY gcp-service-account.json /app/

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . /app/

# Expose the specified port
EXPOSE 8080

# Define the command to run the application
CMD ["python", "app.py"]
