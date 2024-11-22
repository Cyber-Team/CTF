FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install Flask using pip
RUN pip install flask

# Copy the application code
COPY app.py /app/app.py

# Copy the SQLite database
COPY users.db /app/users.db

# Expose port 5000 for Flask
EXPOSE 5003

# Command to run the application
CMD ["python3", "app.py"]

