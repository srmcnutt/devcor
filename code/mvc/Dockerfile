FROM ubuntu:latest

WORKDIR /flask

RUN apt-get update
RUN apt install python3 --yes
RUN ln -s /usr/bin/python3 /usr/bin/python 
RUN apt install python3-pip --yes
RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN pip install flask
RUN export FLASK_ENV=development