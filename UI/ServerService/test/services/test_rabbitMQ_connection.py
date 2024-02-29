import pika
import pytest
from unittest.mock import MagicMock, patch

from src.services.rabbitMQ_connection import RabbitMQConnection


@pytest.fixture
def mock_dependencies():
    with patch("pika.BlockingConnection") as mock_blocking_connection, patch(
        "src.services.rabbitMQ_connection.get_env_instance"
    ) as mock_setup_env:
        mock_env = MagicMock()
        yield mock_blocking_connection, mock_setup_env, mock_env


def test_init_connection(mock_dependencies):
    mock_blocking_connection, mock_setup_env, mock_env = mock_dependencies
    mock_setup_env.return_value = mock_env
    mock_env.RABBITMQ_HOST = "123.45.6.7"
    mock_env.RABBITMQ_PORT = 1234

    rabbitmq_connection = RabbitMQConnection()
    mock_setup_env.assert_called_once()
    rabbitmq_connection.init_connection()

    mock_blocking_connection.assert_called_once_with(
        pika.ConnectionParameters(
            host=mock_env.RABBITMQ_HOST,
            port=mock_env.RABBITMQ_PORT,
        )
    )
    assert rabbitmq_connection.connection == mock_blocking_connection.return_value

    rabbitmq_connection.connection.reset_mock()
    mock_blocking_connection.reset_mock()

    rabbitmq_connection.connection = MagicMock()
    rabbitmq_connection.init_connection()
    mock_blocking_connection.assert_not_called()
    assert rabbitmq_connection.connection is not None


def test_create_channel(mock_dependencies):
    _, mock_setup_env, mock_env = mock_dependencies

    mock_setup_env.return_value = mock_env
    mock_env.RABBITMQ_HOST = "123.45.6.7"
    mock_env.RABBITMQ_PORT = 1234

    rabbitmq_connection = RabbitMQConnection()
    rabbitmq_connection.connection = MagicMock()
    channel = rabbitmq_connection.create_channel()
    assert channel is not None

    rabbitmq_connection.connection.reset_mock()

    rabbitmq_connection.connection = None
    with pytest.raises(Exception, match="No connection to RabbitMQ"):
        channel = rabbitmq_connection.create_channel()
        assert channel is None
