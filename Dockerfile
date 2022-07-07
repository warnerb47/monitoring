FROM python:3.7.13-buster

# configure ansible
RUN apt update && apt install -y nano vim  net-tools curl unzip ansible
# RUN mkdir /root/playbooks

# configure terraform
RUN apt update && apt install -y gnupg software-properties-common curl
RUN curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add -
RUN apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
RUN apt update && apt install terraform

# configure ssh key
RUN mkdir /root/.ssh
COPY .ssh/ /root/.ssh/
RUN chmod 700 /root/.ssh/*

WORKDIR /root
