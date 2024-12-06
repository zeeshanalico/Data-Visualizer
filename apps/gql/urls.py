from django.urls import path
from graphene_django.views import GraphQLView
from .schema import schema  # Import your schema



urlpatterns = [
    path("gql", GraphQLView.as_view(graphiql=True, schema=schema)),  # Attach the schema
]
