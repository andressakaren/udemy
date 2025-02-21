from django.shortcuts import render  # renderizar o arquivo html

# Create your views here.


def home(request):
    print('Home')
    context = {
            'text': 'Olá home'
        }
    return render(
        request,
        'home/index.html',
        context,
    )
