from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get('phone')
        message = request.POST.get("message")
        print(f'{name} - {phone}: {message}')
        return HttpResponse(f'Thank you {name}! Your message success.')
    return render(request, 'catalog/contacts.html')
