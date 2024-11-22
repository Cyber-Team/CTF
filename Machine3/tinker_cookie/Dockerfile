FROM python:3.9-slim

WORKDIR /app

# Add challenge files
COPY app.py /app/app.py

# Install Flask
RUN pip install flask

EXPOSE 5002

CMD ["python", "app.py"]

