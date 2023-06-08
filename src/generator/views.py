from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request, 'generator/index_create.html')


def generate_password(request):
    lower_char = 'abcdefghijklmnopqrstuvwxyz'
    characters = list('abcdefghijklmnopqrstuvwxyz')

    the_password = ''

    if request.GET.get('uppercase'):
        characters.extend(list(lower_char.upper()))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('special_characters'):
        characters.extend(list('!@#$%^&*()'))

    length = int(request.GET.get('length', 6))
    for x in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/generate_password.html', {'password': the_password})


