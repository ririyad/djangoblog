from django.contrib import admin

# Register your models here.
# here Post is the class name from models.posts
from .models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestmp"]
    list_display_links = ["updated"]
    list_editable = ["title"]
    list_filter = ["updated", "timestmp"]
    search_fields = ["title", "content"]

    class Meta:
        model = Post
admin.site.register(Post, PostModelAdmin)
