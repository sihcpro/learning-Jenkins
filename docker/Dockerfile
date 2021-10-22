FROM ubuntu:18.04

RUN apt update

RUN apt install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt install -y python3.8
RUN apt install -y python3.8-dev
RUN apt install -y python3-distutils python3-distutils

RUN apt install -y wget
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3.8 get-pip.py

RUN /usr/bin/python3.8 -m pip install pip -- 
RUN /usr/bin/python3.8 -m pip install pyinotify

RUN pip3 --version

RUN apt install -y libxml2-dev libxslt-dev
RUN apt install -y musl-dev

RUN mkdir -p /src
COPY requirements.txt /src/requirements.txt
RUN pip3 install -r /src/requirements.txt

COPY ./src /src

ENV PYTHONPATH=/src
RUN python3 --version
CMD ["python3.8", "-m", "src"]
