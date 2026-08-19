# Base image using official lightweight Python
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy application files
COPY hello.py /app/hello.py

# Command to execute on container startup
CMD ["python", "hello.py"]
