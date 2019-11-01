from django.urls import path
from .views import Home
from cart.views import  add_to_cart
app_name= 'shopas'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('cart,<slug>', add_to_cart, name='cart'),
]