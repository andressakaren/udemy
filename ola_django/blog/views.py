from django.shortcuts import render

# Create your views here.


def blog(request):
    print('Olá exemplo')
    context = {
        'text': 'Olá blog'
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
