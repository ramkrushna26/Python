from django.shortcuts import render

posts = [
    {
        'author': "Batman",
        'title': 'blog post 1',
        'content': 'my blog post first',
        'date_posted': '24-June-2020'
    },
    {
        'author': "Iron Man",
        'title': 'blog post 2',
        'content': 'my blog post second',
        'date_posted': '24-Auguest-2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})