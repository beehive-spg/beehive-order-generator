FROM node:latest

WORKDIR /app

COPY package.json .

RUN npm install --production

COPY ./lib .

RUN ls

CMD node index.js
