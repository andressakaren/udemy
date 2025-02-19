from django.http import HttpResponse
# from django.shortcuts import render # renderizar o arquivo html

# Create your views here.

def home(request):
    print('Home')
    return HttpResponse('HOME que veio do app criado')
