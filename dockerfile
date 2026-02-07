FROM node:18-alpine

WORKDIR /the/workdir/path

COPY package*.json ./

RUN npm install

COPY . .

CMD ["npm", "test"]