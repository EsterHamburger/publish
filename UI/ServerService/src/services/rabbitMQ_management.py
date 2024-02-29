import json

from services.rabbitMQ_connection import RabbitMQConnection
from models.message_details import message_details
from module.setup_env import get_env_instance


def send_message_to_queue(message_details: message_details):
    try:
        env_value = get_env_instance()
        rabbitMQ_connection = RabbitMQConnection()
        rabbitMQ_connection.init_connection()
        channel = rabbitMQ_connection.create_channel()

        channel.queue_declare(queue=env_value.SEND_QUEUE)
        channel.basic_publish(
            exchange="",
            routing_key=env_value.SEND_QUEUE,
            body=json.dumps(message_details.model_dump()),
        )
    except Exception as error:
        raise error
