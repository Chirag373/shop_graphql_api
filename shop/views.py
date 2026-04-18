from django.shortcuts import render, redirect
from django.contrib import messages
import graphene
from core.schema import schema


def shop_list(request):
    """Display all shops via GraphQL"""
    query = '''
        query {
            allShops {
                id
                name
                address
                emails
                phones
                createdAt
            }
        }
    '''
    
    result = schema.execute(query)
    
    if result.errors:
        error_msg = str(result.errors[0]) if result.errors else 'Unknown error'
        messages.error(request, f'Error: {error_msg}')
        shops = []
    else:
        shops = result.data['allShops'] if result.data else []
    
    return render(request, 'shop/shop_list.html', {'shops': shops})


def shop_detail(request, pk):
    """Display a single shop via GraphQL"""
    query = f'''
        query {{
            shop(id: {pk}) {{
                id
                name
                address
                emails
                phones
                createdAt
                updatedAt
            }}
        }}
    '''
    
    result = schema.execute(query)
    
    if result.errors or not result.data['shop']:
        messages.error(request, 'Shop not found')
        return redirect('shop_list')
    
    shop = result.data['shop']
    return render(request, 'shop/shop_detail.html', {'shop': shop})


def shop_create(request):
    """Create a new shop via GraphQL"""
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        emails_str = request.POST.get('emails', '')
        phones_str = request.POST.get('phones', '')
        
        # Parse comma-separated values
        emails = [e.strip() for e in emails_str.split(',') if e.strip()]
        phones = [p.strip() for p in phones_str.split(',') if p.strip()]
        
        if not name or not address:
            messages.error(request, 'Name and address are required!')
            return render(request, 'shop/shop_form.html', {'mode': 'create'})
        
        # Format GraphQL mutation
        emails_list = ', '.join([f'"{e}"' for e in emails]) if emails else ''
        phones_list = ', '.join([f'"{p}"' for p in phones]) if phones else ''
        
        mutation = f'''
            mutation {{
                createShop(
                    name: "{name}"
                    address: "{address}"
                    emails: [{emails_list}]
                    phones: [{phones_list}]
                ) {{
                    shop {{
                        id
                        name
                    }}
                    success
                    message
                }}
            }}
        '''
        
        result = schema.execute(mutation)
        
        if result.errors:
            messages.error(request, f'Error: {str(result.errors[0])}')
        elif result.data and result.data['createShop']['success']:
            messages.success(request, result.data['createShop']['message'])
            return redirect('shop_list')
        else:
            messages.error(request, result.data['createShop']['message'])
    
    return render(request, 'shop/shop_form.html', {'mode': 'create'})


def shop_update(request, pk):
    """Update an existing shop via GraphQL"""
    # Fetch shop details first
    query = f'''
        query {{
            shop(id: {pk}) {{
                id
                name
                address
                emails
                phones
            }}
        }}
    '''
    
    result = schema.execute(query)
    
    if result.errors or not result.data['shop']:
        messages.error(request, 'Shop not found')
        return redirect('shop_list')
    
    shop = result.data['shop']
    
    if request.method == 'POST':
        name = request.POST.get('name', shop['name'])
        address = request.POST.get('address', shop['address'])
        emails_str = request.POST.get('emails', '')
        phones_str = request.POST.get('phones', '')
        
        emails = [e.strip() for e in emails_str.split(',') if e.strip()]
        phones = [p.strip() for p in phones_str.split(',') if p.strip()]
        
        emails_list = ', '.join([f'"{e}"' for e in emails]) if emails else ''
        phones_list = ', '.join([f'"{p}"' for p in phones]) if phones else ''
        
        mutation = f'''
            mutation {{
                updateShop(
                    id: {pk}
                    name: "{name}"
                    address: "{address}"
                    emails: [{emails_list}]
                    phones: [{phones_list}]
                ) {{
                    shop {{
                        id
                        name
                    }}
                    success
                    message
                }}
            }}
        '''
        
        result = schema.execute(mutation)
        
        if result.errors:
            messages.error(request, f'Error: {str(result.errors[0])}')
        elif result.data and result.data['updateShop']['success']:
            messages.success(request, result.data['updateShop']['message'])
            return redirect('shop_detail', pk=pk)
        else:
            messages.error(request, result.data['updateShop']['message'])
    
    context = {
        'shop': shop,
        'mode': 'update',
        'emails_str': ', '.join(shop['emails']) if shop['emails'] else '',
        'phones_str': ', '.join(shop['phones']) if shop['phones'] else ''
    }
    return render(request, 'shop/shop_form.html', context)


def shop_delete(request, pk):
    """Delete a shop via GraphQL"""
    # Fetch shop details first
    query = f'''
        query {{
            shop(id: {pk}) {{
                id
                name
                address
            }}
        }}
    '''
    
    result = schema.execute(query)
    
    if result.errors or not result.data['shop']:
        messages.error(request, 'Shop not found')
        return redirect('shop_list')
    
    shop = result.data['shop']
    
    if request.method == 'POST':
        mutation = f'''
            mutation {{
                deleteShop(id: {pk}) {{
                    success
                    message
                }}
            }}
        '''
        
        result = schema.execute(mutation)
        
        if result.errors:
            messages.error(request, f'Error: {str(result.errors[0])}')
        elif result.data and result.data['deleteShop']['success']:
            messages.success(request, result.data['deleteShop']['message'])
            return redirect('shop_list')
        else:
            messages.error(request, result.data['deleteShop']['message'])
    
    return render(request, 'shop/shop_confirm_delete.html', {'shop': shop})
