from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# Here I am creating function-based views

def post_home(request):
    return HttpResponse("<h2>Hello!</h2>")
