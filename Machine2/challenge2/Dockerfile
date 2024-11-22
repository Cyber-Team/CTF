FROM python:3.9-slim

# Create working directory
WORKDIR /app

# Add challenge files
COPY app.py /app/app.py

# Install Flask
RUN pip install flask

EXPOSE 5001

CMD ["python", "app.py"]

