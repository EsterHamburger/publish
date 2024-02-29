import pika

from module.setup_env import get_env_instance


class RabbitMQConnection:
    def __init__(self):
        self.connection = None
        self.channel = None
        self.env_value = get_env_instance()

    def init_connection(self):
        try:
            if not self.connection:
                parameters = pika.ConnectionParameters(
                    host=self.env_value.RABBITMQ_HOST, port=self.env_value.RABBITMQ_PORT
                )
                self.connection = pika.BlockingConnection(parameters)
        except Exception as error:
            raise error

    def create_channel(self):
        try:
            if not self.connection:
                raise Exception("No connection to RabbitMQ")
            if not self.channel:
                self.channel = self.connection.channel()
            return self.channel
        except Exception as error:
            raise error
