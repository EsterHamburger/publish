FROM node:20.10
COPY package.json ./
RUN npm install
COPY / .
RUN npm run build
WORKDIR /client
# COPY . /app/
# RUN npm install
# EXPOSE 3000
# RUN npm start

CMD ["cd" ,"client" "npm","start" ]