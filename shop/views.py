from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Shop


def shop_list(request):
    """Display all shops"""
    shops = Shop.objects.all()
    return render(request, 'shop/shop_list.html', {'shops': shops})


def shop_detail(request, pk):
    """Display a single shop"""
    shop = get_object_or_404(Shop, pk=pk)
    return render(request, 'shop/shop_detail.html', {'shop': shop})


def shop_create(request):
    """Create a new shop"""
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        emails = request.POST.get('emails', '').split(',')
        phones = request.POST.get('phones', '').split(',')
        
        # Clean up empty strings
        emails = [e.strip() for e in emails if e.strip()]
        phones = [p.strip() for p in phones if p.strip()]
        
        if name and address:
            Shop.objects.create(
                name=name,
                address=address,
                emails=emails,
                phones=phones
            )
            messages.success(request, 'Shop created successfully!')
            return redirect('shop_list')
        else:
            messages.error(request, 'Name and address are required!')
    
    return render(request, 'shop/shop_form.html', {'mode': 'create'})


def shop_update(request, pk):
    """Update an existing shop"""
    shop = get_object_or_404(Shop, pk=pk)
    
    if request.method == 'POST':
        shop.name = request.POST.get('name', shop.name)
        shop.address = request.POST.get('address', shop.address)
        
        emails = request.POST.get('emails', '').split(',')
        phones = request.POST.get('phones', '').split(',')
        
        shop.emails = [e.strip() for e in emails if e.strip()]
        shop.phones = [p.strip() for p in phones if p.strip()]
        
        shop.save()
        messages.success(request, 'Shop updated successfully!')
        return redirect('shop_detail', pk=shop.pk)
    
    context = {
        'shop': shop,
        'mode': 'update',
        'emails_str': ', '.join(shop.emails),
        'phones_str': ', '.join(shop.phones)
    }
    return render(request, 'shop/shop_form.html', context)


def shop_delete(request, pk):
    """Delete a shop"""
    shop = get_object_or_404(Shop, pk=pk)
    
    if request.method == 'POST':
        shop.delete()
        messages.success(request, 'Shop deleted successfully!')
        return redirect('shop_list')
    
    return render(request, 'shop/shop_confirm_delete.html', {'shop': shop})
