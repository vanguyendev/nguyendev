from django.shortcuts import render
from website.models import *


def home_view(request):
    home_object = HomePage.objects.filter()
    about_object = About.objects.filter()
    services_object = Services.objects.filter()
    portfolio_object = Portfolio.objects.filter()
    contact_object = Contact.objects.filter()
    return render(request, 'home.html', {
        'home_object': home_object,
        'about_object': about_object,
        'services_object': services_object,
        'portfolio_object': portfolio_object,
        'contact_object': contact_object
    })


def base_view(request):
    home_object = HomePage.objects.filter()
    return render(request, 'base.html ', {
        'home_object': home_object
    })
