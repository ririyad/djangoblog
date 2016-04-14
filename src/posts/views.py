from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# Here I am creating function-based views

def post_create(request):
    return HttpResponse("<h2>Create</h2>")


def post_detail(request): # retrieve
    return HttpResponse("<h2>Detail</h2>")


def post_list(request):
    context = {
        "title": "List"
    }
    # if request.user.is_authenticated():
    #     context = {
    #         "title": "My user list!"
    #     }
    # else:
    #     context = {
    #         "title": "Just a list!"
    #     }
    return render(request, "index.html", context)

def post_update(request):
    return HttpResponse("<h2>Update</h2>")

def post_delete(request):
    return HttpResponse("<h2>Delete</h2>")
