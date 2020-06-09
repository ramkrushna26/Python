from django.shortcuts import render 
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields =  ['title', 'author_description', 'content']   

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields =  ['title', 'author_description', 'content']   

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDetailView(DetailView):
    model = Post


def about(request):
    return render(request, 'posts/about.html', {'title': 'about'})
