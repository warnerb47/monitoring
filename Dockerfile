FROM python:3.7.13-buster

# configure aws-cli
RUN apt update && apt install less
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install


WORKDIR /root
