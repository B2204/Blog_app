from django.urls import path

from . import views

urlpatterns = [

    path("", views.home, name="home"),

    path("post/<int:pk>/", views.detail, name="detail"),

    path("create/", views.create, name="create"),

    path("update/<int:pk>/", views.update, name="update"),

    path("delete/<int:pk>/", views.delete, name="delete"),
]