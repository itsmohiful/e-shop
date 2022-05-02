import json

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Category, Order, OrderItem, Product


#home page view
def home(request):
    categories = Category.objects.all()
    
    # category_name = request.GET.get('category')
    # # print(request.GET.get('category'))
    # if category_name:
    #     products = Product.objects.filter(category__slug=category_name)
    #     print(products)
    # else:
    #     products = Product.objects.order_by('-created_at')

    #searching
    if request.method == 'POST':
        query = request.POST.get('query')
        result = Product.objects.filter(Q(name__icontains=query) | Q(price__icontains=query))

        context = {
            'query' : query,
            'results' : result,
            'categories': categories,
        }

        return render(request,'shop/search-result.html',context)

    #pagination
    queryset=Product.objects.all()
    paginator = Paginator(queryset,5)

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context = {
        'products': products,
        'categories': categories,
    }

    return render(request, 'shop/home.html',context)


#show product by categories
def product_by_category(request,slug):
    products = Product.objects.filter(category__slug=slug)
    categories = Category.objects.all()
    context = {
        'products' : products,
        'categories': categories,
    }
    return render(request,'shop/home.html',context)


#adding item in cart
def add_to_cart(request):
    data = json.loads(request.body)
    id = data['id']
    action = data['action']
    customer = request.user.customer
    product = get_object_or_404(Product, id=id)
    order, created = Order.objects.get_or_create(customer=customer, is_complete=False)
    orderitem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'increment':
        orderitem.quantity += 1
    elif action == 'decrement':
        orderitem.quantity -= 1
    orderitem.save()

    if orderitem.quantity <= 0:
        orderitem.delete()

    return JsonResponse({'message' : 'Add to cart successfully'}, safe=False)
    

def cart(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, is_complete=False)
    items = order.orderitem_set.all()
    items_count = order.get_cart_item

    context = {
        'order' : order,
        'items' : items,
        'items_count' : items_count
    }

    return render(request,'shop/cart.html',context)
