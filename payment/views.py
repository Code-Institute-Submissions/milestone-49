from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def payment(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Keep shopping. Your cart is empty.")
        return redirect(reverse('books'))

    order_form = OrderForm()
    template = 'payment/payment.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)