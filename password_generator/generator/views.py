from django.forms import model_to_dict
from django.shortcuts import render
import random

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from generator.serializers import ListPasswordUserSerializer, PasswordCreateSerializer
from generator.models import PasswordsUserList


class ViewPasswordList(APIView):
    def get(self, request):
        queryset = PasswordsUserList.objects.all()
        serializer_class = ListPasswordUserSerializer
        return Response({"data": serializer_class(queryset, many=True).data})

    def post(self, request):
        serializer = PasswordCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'data': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        instance = PasswordsUserList.objects.get(pk=pk)
        serializer = PasswordCreateSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'data': serializer.data})


def home(request):
    return render(request, 'generator/index.html')


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
