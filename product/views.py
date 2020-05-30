from django.shortcuts import render
from product.models import Product
from datetime import datetime
# Create your views here.

def product(request):

    if request.method == "POST":
        name =request.POST.get('name')
        weight =request.POST.get('weight')
        price = request.Post.get('price')
        post=Product(name=name, weight=weight,price=price,created_at=datetime.today(),updated_at = datetime.today)
        post.save()


    return render (request,"post.html")