FROM jupyter/tensorflow-notebook
USER root
COPY ./requirements.txt requirements.txt
ARG JUPYTER_PASSWORD

RUN apt-get update \
  && apt-get install -y \
  gcc

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt
WORKDIR /jupyter/notebooks

ENTRYPOINT jupyter notebook --ip=0.0.0.0 --NotebookApp.token=${JUPYTER_PASSWORD} --allow-root
