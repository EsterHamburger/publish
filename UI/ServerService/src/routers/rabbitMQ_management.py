from fastapi import APIRouter

from services.rabbitMQ_management import send_message_to_queue
from models.message_details import message_details


message_router = APIRouter()


@message_router.post("/")
def send_message(message_details: message_details):
    send_message_to_queue(message_details)
    return {
        "message": "The message sent to RabbitMQ",
        "message_details": message_details,
    }
