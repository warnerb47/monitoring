FROM debian:buster

RUN apt update -y \
    && apt install nginx curl vim -y \
    && apt install software-properties-common -y \
    && apt install snapd -y \
    && snap install core \
    && snap refresh core \

    && snap install --classic certbot \
    && ln -s /snap/bin/certbot /usr/bin/certbot 

    # && add-apt-repository ppa:certbot/certbot -y \
    # && apt-get update -y \
    # && apt-get install python-certbot-nginx -y \
    # && apt-get clean

EXPOSE 80

# STOPSIGNAL SIGTERM

# CMD ["nginx", "-g", "daemon off;"]
CMD [ "/bin/bash" ]

# docker build -t warnerb47/nginx:1.0.0 .