from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('cart/', views.cart, name = 'cart'),
    path('category/<slug:slug>/',views.product_by_category,name='product-by-category'),

    path('add-to-cart',views.add_to_cart,name='add-to-cart'),

]
