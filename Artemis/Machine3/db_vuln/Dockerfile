# Use Python slim image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy necessary files
COPY app.py /app/app.py
COPY users.db /app/users.db

# Install Flask
RUN pip install flask

# Expose the Flask app on port 5000
EXPOSE 5003

# Run the Flask app
CMD ["python", "app.py"]

