import graphene

import tickets.schema


class Query(tickets.schema.Query, graphene.ObjectType):
    pass

class Mutation(tickets.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
