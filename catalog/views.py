from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from catalog.models import Product

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get('phone')
        message = request.POST.get("message")
        print(f'{name} - {phone}: {message}')
        return HttpResponse(f'Thank you {name}! Your message success.')
    return render(request, 'catalog/contacts.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'catalog/home.html', {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'catalog/product.html', {'product': product})
