FROM ubuntu:20.04

RUN apt update && apt install -y gcc
COPY bin_password.c /bin_password.c
RUN gcc /bin_password.c -o /bin_password && strip /bin_password && rm /bin_password.c

CMD ["/bin_password"]

