from django.shortcuts import render 
from django.views.generic import CreateView, ListView
from .models import Post

def home(request):
    context = {
        'post_s': Post.objects.all()
    }
    return render(request, 'posts/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = "posts/home.html"
    context_object_name = 'post_s'
    ordering = ['-posted_on']


class PostCreateView(CreateView):
    model = Post
    fields =  ['title', 'author_description', 'content']   

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'posts/about.html', {'title': 'about'})
