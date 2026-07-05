import pytest

from django.contrib.auth.models import User


@pytest.mark.django_db
def test_jwt_login(api_client):

    User.objects.create_user(
        username="admin",
        password="password123"
    )

    response = api_client.post(
        "/api/token/",
        {
            "username": "admin",
            "password": "password123",
        },
    )

    assert response.status_code == 200

    assert "access" in response.data

    assert "refresh" in response.data