from django.shortcuts import render
# from . import data
from blog.data import posts

# Create your views here.


def blog(request):
    print('Olá exemplo')
    context = {
        # 'posts': 'data.posts'
        'posts': posts
        
    }
    return render(
        request,
        'blog/index.html',
        context,
    )


def exemplo(request):
    print('Olá exemplo')
    context = {
        'text': 'Olá exemplo', 
        'title': 'Essa é um exemplo - '
    }
    return render(
        request,
        'blog/exemplo.html',
        context,
    )
