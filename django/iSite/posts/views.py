from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostCreateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    context = {
        'post_s': Post.objects.all()
    }
    return render(request, 'posts/home.html', context)


@login_required
def postCreate(request):
    form = PostCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.author = request.user
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, f'Post Created')
        return redirect(instance.get_absolute_url())
    return render(request, 'posts/post_form.html', {'form': form})


class PostListView(ListView):
    model = Post
    template_name = "posts/home.html"
    context_object_name = 'post_s'
    ordering = ['-posted_on']



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
