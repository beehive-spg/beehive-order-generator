FROM python:3-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY order-generator .

ARG settings_queue
ARG order_queue
ARG rabbitmq
ARG database

ENV SETTINGS_QUEUE=$settings_queue
ENV ORDER_QUEUE=$order_queue
ENV RABBITMQ_URL=$rabbitmq
ENV DATABASE_URL=$database

CMD python3 order-generator.py send 7 20