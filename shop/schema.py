import graphene

from shop.mutations import CreateShop, UpdateShop, DeleteShop
from .types import ShopType
from .models import Shop

class Query(graphene.ObjectType):
    all_shops = graphene.List(ShopType)
    shop = graphene.Field(ShopType, id=graphene.ID(required=True))

    def resolve_all_shops(self, info):
        return Shop.objects.all()
    
    def resolve_shop(self, info, id):
        try:
            return Shop.objects.get(pk=id)
        except Shop.DoesNotExist:
            return None

class Mutation(graphene.ObjectType):
    create_shop = CreateShop.Field()
    update_shop = UpdateShop.Field()
    delete_shop = DeleteShop.Field()
