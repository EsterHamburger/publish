FROM node:20.10
# COPY package.json ./
# RUN npm install
# COPY / .
# RUN npm run build
WORKDIR /app
COPY . /app/
# RUN npm start
RUN npm install
EXPOSE 3000
CMD [ "npm","start" ]