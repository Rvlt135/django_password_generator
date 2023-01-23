from django.shortcuts import render
from django.http import HttpResponse


def main_screen(request):
    return render(request, 'generator/main.html')


def password(request):
    return render(request, 'generator/password.html')
