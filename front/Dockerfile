FROM httpd:2.4
RUN apt update
RUN apt install -y iputils-ping
RUN apt install -y curl
EXPOSE 80
COPY . /usr/local/apache2/htdocs/
