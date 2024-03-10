# Use the official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the application code to the working directory
COPY . /app/

# Expose the port on which the application will run
EXPOSE 50052

# Run GRPC Server
CMD ["python3", "/app/gprc_server.py"]