FROM python:3.9-slim

# Install necessary tools
RUN apt-get update && apt-get install -y curl

# Create working directory
WORKDIR /app

# Add challenge files
COPY index.html /app/index.html

# Install and run Flask server
RUN pip install flask
COPY app.py /app/app.py

EXPOSE 5000

CMD ["python", "app.py"]

