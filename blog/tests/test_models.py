import pytest

from django.contrib.auth.models import User

from blog.factories import PostFactory, AuthorFactory


@pytest.mark.django_db
def test_post_creation():
    post = PostFactory()

    # Verify the object was created
    assert post.id is not None

    # Verify factory values
    assert post.title.startswith("Post")
    assert post.content == "Learning Django"

    # Verify author exists
    assert post.author is not None


@pytest.mark.django_db
def test_create_post(api_client):

    from django.contrib.auth.models import User

    # Create a user
    user = User.objects.create_user(
        username="admin",
        password="admin123"
    )

    # Login the API client
    api_client.force_authenticate(user=user)

    # Create an author
    author = AuthorFactory()

    # Call the API
    response = api_client.post(
        "/api/posts/",
        {
            "title": "Python",
            "content": "DRF Testing",
            "author": author.id,
        },
        format="json",
    )

    print("Status Code:", response.status_code)
    print("Response:", response.data)

    assert response.status_code == 201