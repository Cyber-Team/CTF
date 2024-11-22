FROM ubuntu:20.04
RUN useradd hacker && echo "hacker:hacker123" | chpasswd
RUN echo "hacker ALL=(ALL) NOPASSWD: /usr/bin/less" >> /etc/sudoers
RUN echo "ctf_{Escalate_To_Sudo}" > /root/flag.txt
CMD ["/bin/bash"]
