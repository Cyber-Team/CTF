# Use a base image with basic utilities
FROM ubuntu:latest

# Install necessary tools
RUN apt-get update && apt-get install -y \
    gcc \
    gdb \
    strace \
    ltrace \
    && rm -rf /var/lib/apt/lists/*

# Copy challenges into the container
COPY challenge1 /opt/challenge1
COPY challenge2 /opt/challenge2
COPY challenge3 /opt/challenge3
COPY start.sh /opt/start.sh

# Make the start script executable
RUN chmod +x /opt/start.sh
RUN chmod +x /opt/challenge1/solve_me_1
RUN chmod +x /opt/challenge2/solve_me_2
RUN chmod +x /opt/challenge3/solve_me_3

# Start the challenges on container run
CMD ["/opt/start.sh"]
