FROM python:3.8-alpine
# FROM ubuntu:18.04

LABEL maintainer="ari -- dev.to https://dev.to/ari_hacks"

# COPY run.sh .

# RUN apt-get update -y && \
#     apt-get -y install sudo && \
#     apt-get install -y python3-pip && \
#     bash ./run.sh && \
#     apt-get install python3-dev

RUN apk add --no-cache --virtual \
      .build-deps \
      gcc \
      musl-dev \
      linux-headers \
      pkgconfig poppler-utils \
      build-base \
      alpine-sdk \
      poppler-dev 
    #   python3-tkinter 


COPY requirements.txt .

COPY input.pdf .

RUN pip3 install -r requirements.txt

COPY main.py .

CMD [ "python3", "main.py"] 
