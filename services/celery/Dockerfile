FROM ubuntu:20.04
LABEL maintainer="Antoine Treudsky " email="antoine@treudsky.com"
ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY . /celery
WORKDIR /celery
RUN ls
RUN apt-get update \
    #Adding tesseract
    && apt-get install tesseract-ocr -y \
    #Adding support for French
    tesseract-ocr-fra\
    #Adding libnfs client
    libnfs-utils \
    libnfs-dev \
    python3 \
    #python-setuptools \
    python3-pip \
    && apt-get clean \
    && apt-get autoremove

#COPY ./requirements.txt /celery/requirements.txt

RUN pip install -r requirements.txt