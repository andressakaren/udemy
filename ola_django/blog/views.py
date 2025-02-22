from django.shortcuts import render
# from . import data
from blog.data import posts
from typing import Any 
from django.http import HttpRequest

# Create your views here.


def blog(request):
    print('blog')
    context = {
        # 'posts': 'data.posts'  --- se a importação for da outra forma comentada
        'posts': posts
        
    }
    return render(
        request,
        'blog/index.html',
        context,
    )

def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None
    
    for post in posts:
        if post['id'] == post_id:
            found_post = post    
            break
        
    if found_post is None:
        raise Exception('Não EXISTE')
        
        
    context = {
        'post': found_post,
        'title': found_post['title'] + ' - '
    }
    
    return render(
        request,
        'blog/post.html',
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
