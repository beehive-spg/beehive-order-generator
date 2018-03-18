FROM python:3-alpine

RUN mkdir -p /beehive-order-generator

ARG google_api_key
ARG order_queue
ARG rabbitmq
ARG database

ENV GOOGLE_API_KEY=$google_api_key
ENV ORDER_QUEUE=$order_queue
ENV RABBITMQ_URL=$rabbitmq
ENV DATABASE_URL=$database

COPY /src /beehive-order-generator/src
COPY requirements.txt /beehive-order-generator

RUN pip3 install -r beehive-order-generator/requirements.txt

WORKDIR /beehive-order-generator/src

ENTRYPOINT [ "python3", "order-generator.py", "send", "100", "20" ]