# grpcServer/grpcDockerfile

# Use the official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the common requirements file to the working directory
COPY ../requirements.txt requirements.txt

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the application code to the working directory
OPY ../grpcServer/ /app/

# Expose the port on which the application will run
EXPOSE 50052

# Run GRPC Server
CMD ["python3", "grpc_server.py"]
