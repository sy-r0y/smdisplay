
# MAP THE URL TO THE VIEW FUNCTION

from django.urls import path
from . import views

urlpatterns = [

    path('', views.index),

]