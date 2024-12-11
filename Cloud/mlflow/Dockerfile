#FROM python:3.7-slim-buster
FROM python:3.10.6-slim-buster

USER root

COPY ./requirements.txt requirements.txt

RUN apt-get update 

RUN pip3 install --upgrade pip

# Install python packages
RUN pip3 install -r requirements.txt 
