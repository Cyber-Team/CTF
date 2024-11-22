# Use an official Debian image as a base
FROM debian:latest

# Set up the environment
RUN mkdir -p /ctf
WORKDIR /ctf

# Copy the password-check script
COPY check_password.sh /ctf/check_password.sh
RUN chmod +x /ctf/check_password.sh

# Set the entrypoint to run the password-check script
ENTRYPOINT ["/ctf/check_password.sh"]
