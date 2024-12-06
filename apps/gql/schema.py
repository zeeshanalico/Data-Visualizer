import graphene

# Define a Dummy User Type
class UserType(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    email = graphene.String()

# Define a Query for Dummy Data
class Query(graphene.ObjectType):
    users = graphene.List(UserType)  # Define a query for a list of users

    def resolve_users(self, info):
        # Dummy data
        return [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "email": "bob@example.com"},
        ]

# Define the Schema
schema = graphene.Schema(query=Query)
