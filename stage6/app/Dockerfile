FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y openssh-server gcc sudo && rm -rf /var/lib/apt/lists/*
RUN useradd -m -s /bin/bash ftpuser && echo "ftpuser:Str0ngFTPpass!" | chpasswd
COPY vuln_binary.c /tmp/vuln_binary.c
RUN gcc -o /usr/local/bin/syscheck /tmp/vuln_binary.c && \
    chown root:root /usr/local/bin/syscheck && \
    chmod 4755 /usr/local/bin/syscheck
RUN echo "AEGIS{root_access_granted}" > /root/flag.txt && chmod 600 /root/flag.txt
RUN mkdir /var/run/sshd
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
