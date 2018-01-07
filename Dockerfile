FROM node:latest

#ARG node_env=production
#ENV NODE_ENV=$node_env

WORKDIR /app

COPY package.json .

RUN npm install --production

COPY ./lib .

RUN ls

CMD node index.js
