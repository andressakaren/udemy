from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.

def blog(request):
    print('Olá mundo')
    return HttpResponse('BLOG que veio do app 1')

def exemplo(request):
    print('Olá mundo')
    return HttpResponse('Exemplo que veio do app 1')