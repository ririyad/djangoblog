from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import PostForm
from .models import Post

# Create your views here.
# Here I am creating function-based views


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())

    # if request.method == "POST":
    #     print request.POST.get("content")
    #     print request.POST.get("title")
        context = {
            "form": form,
            }
    else:
        messages.error(request, "Not Successfully Created")
        context = {
            "form": form
        }

    return render(request, "post_form.html", context)


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


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # message success
        messages.success(request, "<a href='#'>Items</a> Saved!", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form
    }
    return render(request, "post_form.html", context)


def post_delete(request):
    return HttpResponse("<h2>Delete</h2>")
