FROM node:20.10
COPY client/package.json ./
RUN npm install
COPY client .
RUN npm run build
RUN npm run build
WORKDIR /app
COPY . /app/
RUN npm start