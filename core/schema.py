import graphene
import shop.schema as shop_schema

class Query(shop_schema.Query, graphene.ObjectType):
    pass

class Mutation(shop_schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
