from django.shortcuts import render 
from django.views.generic import CreateView, ListView
from .models import Post

def home(request):
    context = {
        'post-s': Post.objects.all()
    }
    return render(request, 'posts/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = "posts/home.html"
    context_object_name = 'post-s'
    ordering = ['-posted_on']
    


def about(request):
    return render(request, 'posts/about.html', {'title': 'about'})
