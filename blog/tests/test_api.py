import pytest

from django.contrib.auth.models import User

from blog.factories import PostFactory


@pytest.mark.django_db
def test_get_posts(api_client):

    # Create a user
    user = User.objects.create_user(
        username="admin",
        password="admin123"
    )

    # Authenticate the client
    api_client.force_authenticate(user=user)

    # Create some posts
    PostFactory.create_batch(3)

    # Call the API
    response = api_client.get("/api/posts/")

    assert response.status_code == 200
    assert len(response.data) == 3