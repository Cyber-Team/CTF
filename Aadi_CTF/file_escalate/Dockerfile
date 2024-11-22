FROM ubuntu:20.04

# Create file and misconfigured sudoers
RUN echo "ctf_{SuDo_FILe_AcCESs_ExPloIt}" > /etc/secret.txt \
    && echo 'hacker ALL=(ALL) NOPASSWD: /bin/cat /etc/secret.txt' >> /etc/sudoers

CMD ["/bin/bash"]

