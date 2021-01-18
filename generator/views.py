from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    number_list = list(range(6,13))
    return render(request,'generator/home.html',{'number_list':number_list})

def about(request):
    return render(request,'generator/about.html')

def password(request):
    generate_password = ''
    length = int(request.GET.get('length',12))
    characters = list('abcdefghijklmnopqrstuvwxys')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('uppercase'):
        characters.extend(list('0123456789'))
    
    for i in range(length):
        generate_password += random.choice(characters) 
    return render(request, 'generator/password.html',{'password':generate_password})