FROM python:3.7-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .
RUN apk add build-base
RUN pip install -r requirements.txt
CMD tail -f /dev/null
