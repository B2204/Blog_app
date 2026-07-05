import factory

from blog.models import Author, Post


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.Sequence(lambda n: f"John {n}")
    email = factory.Sequence(lambda n: f"john{n}@example.com")


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Sequence(lambda n: f"Post {n}")
    content = "Learning Django"

    author = factory.SubFactory(AuthorFactory)