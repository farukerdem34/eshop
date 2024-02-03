from django.shortcuts import render
from app.models import Product
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
    order = r.GET.get('order')  
    if order not in ['date','rating','popularity']:
        order = 'null'
    query = f"SELECT * FROM app_product ORDER BY {order}"
    products = Product.objects.raw(query)
    return render(r,'shop.html',{
        "products":products
    })