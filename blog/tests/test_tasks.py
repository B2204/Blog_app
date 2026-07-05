from unittest.mock import patch


@patch("blog.tasks.send_welcome_email")
def test_send_email(mock_send):

    mock_send("barath@gmail.com")

    mock_send.assert_called_once_with(
        "barath@gmail.com"
    )