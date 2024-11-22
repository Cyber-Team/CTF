# Use an official Debian image as a base
FROM debian:latest

# Set up the environment
RUN mkdir -p /ctf
WORKDIR /ctf

# Create a flag file and hide it in a random directory
RUN mkdir -p /hidden/directory/structure && \
    echo "CTF_{file_hunt_success}" > /hidden/directory/structure/flag.txt

# Set the entrypoint to bash so users can interact with the container
ENTRYPOINT ["/bin/bash"]
