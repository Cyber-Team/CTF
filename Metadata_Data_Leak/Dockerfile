# Use a lightweight Ubuntu base image
FROM ubuntu:latest

# Set environment variables
ENV FLAG="ctf_{metadata_leak_detected}"

# Install necessary tools
RUN apt-get update && \
    apt-get install -y exiftool && \
    apt-get clean

# Set the working directory
WORKDIR /challenge

# Copy entrypoint script and image to the container
COPY entrypoint.sh /challenge/
COPY secret_image.jpg /challenge/

# Make the script executable
RUN chmod +x /challenge/entrypoint.sh

# Run entrypoint script on container start
CMD ["/challenge/entrypoint.sh"]
