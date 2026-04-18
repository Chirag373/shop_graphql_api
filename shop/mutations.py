import graphene
from .types import ShopType
from .models import Shop
from .validation import validate_emails, validate_phones

import graphene
from .types import ShopType
from .models import Shop
from .validation import validate_emails, validate_phones

class CreateShop(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        emails = graphene.List(graphene.String, required=False)
        phones = graphene.List(graphene.String, required=False)
        address = graphene.String(required=True)

    shop = graphene.Field(ShopType)
    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, name, address, emails=None, phones=None):
        emails = emails or []
        phones = phones or []
        
        # Validate only if provided
        if emails:
            valid_emails, email_msg = validate_emails(emails)
            if not valid_emails:
                return CreateShop(
                    shop=None,
                    success=False,
                    message=email_msg
                )
        
        if phones:
            valid_phones, phone_msg = validate_phones(phones)
            if not valid_phones:
                return CreateShop(
                    shop=None,
                    success=False,
                    message=phone_msg
                )
        
        shop = Shop.objects.create(
            name=name,
            emails=emails,
            phones=phones,
            address=address
        )
        return CreateShop(
            shop=shop,
            success=True,
            message=f"Shop '{shop.name}' created successfully!"
        )
    
class UpdateShop(graphene.Mutation):

    class Arguments:
        id      = graphene.ID(required=True)
        name    = graphene.String()
        emails  = graphene.List(graphene.String)
        phones  = graphene.List(graphene.String)
        address = graphene.String()

    shop    = graphene.Field(ShopType)
    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, id, name=None, emails=None, phones=None, address=None):
        try:
            shop = Shop.objects.get(pk=id)
        except Shop.DoesNotExist:
            return UpdateShop(shop=None, success=False, message=f"Shop with id {id} not found.")

        # Validate emails if provided
        if emails:
            valid_emails, email_msg = validate_emails(emails)
            if not valid_emails:
                return UpdateShop(shop=None, success=False, message=email_msg)

        # Validate phones if provided
        if phones:
            valid_phones, phone_msg = validate_phones(phones)
            if not valid_phones:
                return UpdateShop(shop=None, success=False, message=phone_msg)

        if name    is not None: shop.name    = name
        if emails  is not None: shop.emails  = emails
        if phones  is not None: shop.phones  = phones
        if address is not None: shop.address = address

        shop.save()

        return UpdateShop(
            shop    = shop,
            success = True,
            message = f"Shop '{shop.name}' updated successfully!"
        )
    
class DeleteShop(graphene.Mutation):

    class Arguments:
        id = graphene.ID(required=True)

    success    = graphene.Boolean()
    message    = graphene.String()
    deleted_id = graphene.ID()

    def mutate(self, info, id):
        try:
            shop = Shop.objects.get(pk=id)
        except Shop.DoesNotExist:
            return DeleteShop(
                success    = False,
                message    = f"Shop with id {id} not found.",
                deleted_id = None
            )

        shop_name = shop.name   # capture before deletion
        shop.delete()

        return DeleteShop(
            success    = True,
            message    = f"Shop '{shop_name}' deleted successfully!",
            deleted_id = id
        )