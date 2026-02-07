FROM node:18-alpine

WORKDIR /the/workdir/path

COPY package*.json ./

RUN npm install

RUN npm install --save-dev jest

COPY . .

CMD ["npm" , "test"]