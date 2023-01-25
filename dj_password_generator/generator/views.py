from django.shortcuts import render
import random
from django.http import HttpResponse

def main_screen(request):
    thepassword = 'test'
    return render(request, 'generator/main.html', {'password': thepassword})


def password_generated(request):
    characters = list('')
    uppercase = list('ABCDEFGHIGKLMNOPQRSTUVYXWZ')
    lowercase = list('abcdefghigklmnopqrstuvyxwz')
    include_number = list('1234567890')
    lenght = int(request.GET.get('lenght', 12))
    if request.GET.get('uppercase'):
        characters.extend(uppercase)
    if request.GET.get('lowercase'):
        characters.extend(lowercase)
    if request.GET.get('number'):
        characters.extend(include_number)

    thepassword = ''
    for it in range(lenght):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})

'''    pas = ''
    
    for x in range(16):  # Количество символов (16)
        pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
    return render(request, 'generator/password.html', {'password': thepassword})'''
