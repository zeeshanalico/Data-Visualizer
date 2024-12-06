from django.urls import path
from graphene_django.views import GraphQLView
from django.conf.urls import include


urlpatterns = [
    path("user/",include('apps.user.urls') ),  # Attach the schema
]
