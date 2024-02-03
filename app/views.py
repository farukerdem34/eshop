from django.shortcuts import render

# Create your views here.

def cart(r):
    return render(r,'cart.html')

def checkout(r):
    return render(r,'checkout.html')

def contact(r):
    return render(r,'contact.html')

def detail(r):
    return render(r,'detail.html')

def index(r):
    return render(r,'index.html')

def shop(r):
    return render(r,'shop.html')