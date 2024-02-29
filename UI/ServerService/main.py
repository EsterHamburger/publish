from fastapi import FastAPI
from routers.rabbitMQ_management import message_router

app = FastAPI()

app.include_router(message_router, prefix="/send_message")
