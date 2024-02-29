from unittest.mock import patch

from src.models.message_details import message_details
from src.routers.rabbitMQ_management import send_message


def test_send_message():
    with patch(
        "src.routers.rabbitMQ_management.send_message_to_queue"
    ) as mock_send_message_to_queue:
        mock_message_details = message_details(
            name="name",
            shapefile_path="shapefile_path",
            tiffs_path="tiffs_path",
            sensor="sensor",
            logs_path="logs_path",
        )
        result = send_message(mock_message_details)
        mock_send_message_to_queue.assert_called_once_with(mock_message_details)

    assert result == {
        "message": "The message sent to RabbitMQ",
        "message_details": mock_message_details,
    }
