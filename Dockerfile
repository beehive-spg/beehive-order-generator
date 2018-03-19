FROM python:3-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY src .

ARG google_api_key
ARG order_queue
ARG rabbitmq
ARG database

ENV GOOGLE_API_KEY=$google_api_key
ENV ORDER_QUEUE=$order_queue
ENV RABBITMQ_URL=$rabbitmq
ENV DATABASE_URL=$database

CMD python3 order-generator.py send 100 20