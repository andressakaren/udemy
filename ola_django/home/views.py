from django.shortcuts import render  # renderizar o arquivo html

# Create your views here.


def home(request):
    print('Home')
    return render(
        request,
        'home/index.html'
    )
