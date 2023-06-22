FROM python:3.10-bullseye

COPY src/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && rm -f /tmp/requirements.txt

RUN mkdir /kedro
WORKDIR /kedro
COPY . .
