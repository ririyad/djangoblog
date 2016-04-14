from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.
# Here I am creating function-based views

def post_create(request):
    return HttpResponse("<h2>Create</h2>")


def post_detail(request, id=None): # retrieve
    # instance = Post.objects.get(id=1)
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "post_detail.html", context)


def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
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
