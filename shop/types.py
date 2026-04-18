import graphene
from graphene_django import DjangoObjectType
from .models import Shop

class ShopType(DjangoObjectType):
    emails = graphene.List(graphene.String)
    phones = graphene.List(graphene.String)

    class Meta:
        model = Shop
        fields = ("id", "name", "emails", "phones", "address", "created_at", "updated_at")

    def resolve_emails(self, info):
        emails = self.emails
        return emails if emails and isinstance(emails, list) else []
    
    def resolve_phones(self, info):
        phones = self.phones
        return phones if phones and isinstance(phones, list) else []