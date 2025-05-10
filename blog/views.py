from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')  # Get published posts ordered by creation date
    template_name = "blog/index.html"  # Specify the template
    context_object_name = 'posts'  # This will make the posts available in the template as 'posts'
    paginate_by = 6
