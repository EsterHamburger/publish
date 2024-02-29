FROM node:16-alpine as frontend

COPY client/package.json ./
RUN npm install

COPY client .
RUN npm run build


FROM unit:1.31.1-python3.11

COPY config.json /docker-entrypoint.d/config.json
COPY  --from=frontend /build ./static

COPY ./ServerService /app

WORKDIR /app

RUN python -m pip install --upgrade pip && \
    pip3 install -e .

EXPOSE 8080
