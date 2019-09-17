import graphene
from .lead.schema import Query as leadQuery


class Query(leadQuery, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = graphene.Schema(query=Query)
