
# URL MAPPING done here @ urls.py

# MAP the URL to the VIEW FUNCTION

# urlpatterns is  BY-CONVENTION
# urlpatterns is used to define various URLs to their view function


from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path() maps url to view function. 1st argument is url endpoint
    # 1st argument of path() is a string that specifies URL endpoint
    # 2ns argument of path() specifies the VIEW FUNCTION
    path('', views.BoardHomeView.as_view(), name='home'),
    path('buynow', views.buy_now, name='buy-now'),
    path('productdetail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('addtocart', views.add_to_cart, name='add-to-cart'),
    path('checkout', views.checkout, name='checkout'),
    path('profile', views.profile, name='profile'),
    path('address', views.address, name='address'),
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('home', views.BoardHomeView.as_view(), name='home'),
    path('changepassword', views.change_password, name='change-password'),
    path('orders', views.orders, name='orders'),
    path('mobile/<slug:category>', views.MobileView.as_view(), name='mobiledata'),
    path('mobile', views.MobileView.as_view(), name='mobile'), 
  
] 