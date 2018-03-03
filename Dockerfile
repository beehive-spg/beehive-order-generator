FROM python:3

RUN mkdir -p /beehive-order-generator

COPY /src /beehive-order-generator/src
COPY requirements.txt /beehive-order-generator
COPY .env /beehive-order-generator

RUN pip3 install -r beehive-order-generator/requirements.txt

WORKDIR /beehive-order-generator/src

ENTRYPOINT [ "python3", "order-generator.py", "sendsaved", "0" ]