# used the alpine-based python image, so I didn't have to install python from scratch.
FROM python:3.7-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .

# install package dependancies
RUN apk add build-base

# install python dependancies
RUN pip install -r requirements.txt

# default command to keep the container running
CMD tail -f /dev/null
