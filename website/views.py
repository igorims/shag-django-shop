from django.shortcuts import render, redirect
from cloudipsp import Api, Checkout

from .models import Product


def index(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'website/index.html', context)


def about(request):
    return render(request, 'website/about.html')


def create(request):
    if request.method == 'POST':
        product = Product(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            price=request.POST.get('price'),
        )
        product.save()
        return redirect('index')
    return render(request, 'website/create.html')


def buy_product(request, pk):
    product = Product.objects.get(id=pk)

    api = Api(merchant_id=1396424, secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "RUB",
        "amount": str(product.price) + '00'
    }
    url = checkout.url(data).get('checkout_url')
    return redirect(url)





def delete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect("index")
