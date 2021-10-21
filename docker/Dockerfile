FROM python:3.8.12-alpine3.14

RUN apk update
RUN apk add gcc
RUN apk add libxml2-dev libxslt-dev
RUN apk add musl-dev

RUN mkdir -p /src
COPY requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt

COPY ./src /src

ENV PYTHONPATH=/src
CMD ["python", "-m", "src"]

