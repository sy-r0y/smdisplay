from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# What should the user see when they navigate to a certain page

# define your VIEW FUNCTIONs

# all VIEW FUNCTION take in the parameter 'request' ie HttpRequest that is passed to this view function


def index(request):
    response = HttpResponse('Boards Index View Function')
    return response
