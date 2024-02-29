import os
from dotenv import load_dotenv

load_dotenv()


class _SetupEnv:
    def init_settings(self):
        try:
            self.RABBITMQ_HOST: str = os.environ["RABBITMQ_HOST"]
            self.RABBITMQ_PORT: str = os.environ["RABBITMQ_PORT"]
            self.USERNAME: str = os.environ["USERNAME"]
            self.PASSWORD: str = os.environ["PASSWORD"]
            self.SEND_QUEUE: str = os.environ["SEND_QUEUE"]
            self.SERVICE_NAME: str = os.environ["SERVICE_NAME"]
        except KeyError as e:
            raise ValueError(f"Missing key in env file: {e}")
        return self


env = None


def get_env_instance():
    global env
    if env is None:
        env = _SetupEnv().init_settings()
    return env
