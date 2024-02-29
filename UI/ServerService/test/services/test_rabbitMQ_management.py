import json
import pytest
from unittest.mock import MagicMock, patch

from src.models.message_details import message_details
from src.services.rabbitMQ_management import send_message_to_queue


@pytest.fixture
def mock_dependencies():
    with patch(
        "src.services.rabbitMQ_management.RabbitMQConnection", return_value=MagicMock()
    ) as mock_rabbitMQ_connection, patch(
        "src.services.rabbitMQ_management.get_env_instance"
    ) as mock_setup_env:
        mock_message_details = message_details(
            name="name",
            shapefile_path="shapefile_path",
            tiffs_path="tiffs_path",
            sensor="sensor",
            logs_path="logs_path",
        )
        mock_env = MagicMock()
        yield mock_rabbitMQ_connection(), mock_setup_env, mock_message_details, mock_env


def test_send_message_to_queue(mock_dependencies):
    (
        mock_rabbitMQ_connection,
        mock_setup_env,
        mock_message_details,
        mock_env,
    ) = mock_dependencies
    mock_channel = mock_rabbitMQ_connection.create_channel.return_value = MagicMock()

    mock_setup_env.return_value = mock_env
    mock_env.SEND_QUEUE = "SEND_QUEUE"

    send_message_to_queue(mock_message_details)
    mock_setup_env.assert_called_once()

    mock_rabbitMQ_connection.init_connection.assert_called_once()
    mock_rabbitMQ_connection.create_channel.assert_called_once()
    mock_channel.queue_declare.assert_called_once_with(queue=mock_env.SEND_QUEUE)
    mock_channel.basic_publish.assert_called_once_with(
        exchange="",
        routing_key=mock_env.SEND_QUEUE,
        body=json.dumps(mock_message_details.model_dump()),
    )
