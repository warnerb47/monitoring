FROM python:3.7.13-buster
RUN apt update && apt install -y nano vim  net-tools curl ansible
RUN mkdir /root/.ssh && mkdir /root/playbooks
COPY .ssh/ /root/.ssh/
RUN chmod 700 /root/.ssh/*
COPY config/ /etc/ansible/
COPY playbooks/ /root/playbooks/
WORKDIR /root/playbooks


# docker build -t monitoring .
# docker run --rm -ti monitoring bash