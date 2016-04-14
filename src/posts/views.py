from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# Here I am creating function-based views

def post_create(request):
    return HttpResponse("<h2>Create</h2>")

def post_detail(request): # retrieve
    return HttpResponse("<h2>Detail</h2>")

def post_list(request):
    return render(request, "index.html", {})

def post_update(request):
    return HttpResponse("<h2>Update</h2>")

def post_delete(request):
    return HttpResponse("<h2>Delete</h2>")
