from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PostList(ListView):
    model = Post
    # queryset = Post.objects.filter(status=1).order_by('-created_on')
    queryset = Post.objects.all()
    template_name = "post_list.html"
