from django.shortcuts import render

from .models import Category, Product


#home page view
def home(request):
    categories = Category.objects.all()
    
    category_id = request.GET.get('category')
    # print(request.GET.get('category'))
    if category_id:
        products = Product.objects.filter(category=category_id)
    else:
        products = Product.objects.order_by('-created_at')

    context = {
        'products': products,
        'categories': categories,
    }

    return render(request, 'shop/home.html',context)
