
# URL MAPPING done here @ urls.py

# MAP the URL to the VIEW FUNCTION

# urlpatterns is  BY-CONVENTION
# urlpatterns is used to define various URLs to their view function


from django.urls import path
from . import views

urlpatterns = [
    # path() maps url to view function. 1st argument is url endpoint
    # 1st argument of path() is a string that specifies URL endpoint
    # 2ns argument of path() specifies the VIEW FUNCTION
    path('', views.index),
    path('buynow/', views.buynow),
    path('productdetail', views.product_detail, name='product-detail'),
    path('addtocart', views.add_to_cart, name='add-to-cart'),
    path('buynow', views.buy_now, name='buy-now'),
    path('checkout', views.checkout, name='checkout'),

    
]