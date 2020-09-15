from django.shortcuts import render
from django.conf import settings

def index(request):
    """ A view to return the index.html page """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    print(stripe_public_key)
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    print(stripe_secret_key)

    return render(request, 'home/index.html')
