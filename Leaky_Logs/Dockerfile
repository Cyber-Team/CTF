# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install necessary dependencies (for example, Flask)
RUN pip install Flask

# Make port 80 available to the world outside the container
EXPOSE 80

# Define environment variable for the log file
ENV LOG_FILE=/usr/src/app/access.log

# Run the application
CMD ["python", "server.py"]
