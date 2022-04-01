from django.shortcuts import render

from .models import Category, Product


#home page view
def home(request):
    categories = Category.objects.all()
    products = Product.objects.order_by('-created_at')

    context = {
        'products': products,
        'categories': categories,
    }

    return render(request, 'shop/home.html',context)
