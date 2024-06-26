import graphene
import gql.schema

"""
It hold, via inheritence, all the Queries and future operations, created:
"""
class Query(gql.schema.Query, graphene.ObjectType):
    pass


class Mutation(gql.schema.Mutation, graphene.ObjectType):
    ...


# NOTE: create the `schema` variable
"""
The `SCHEMA` settings, defined in the `settings.py` points to this variable

file: shorty/settings.py
GRAPHENE = {
    'SCHEMA': 'shorty.schema.schema',
}
"""
schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)