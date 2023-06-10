from django.shortcuts import render
from django.http import HttpResponse
import random

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from generator.serializers import ListPasswordSerializer
from generator.models import ListPasswords


class ListPasswordViewSet(ModelViewSet):
    """
    Get all objects from db and filter query request
    filter_backends init class filters
    filterset filter for query
    search field
    filters for value ordering rings
    """
    queryset = ListPasswords.objects.all()
    serializer_class = ListPasswordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    #filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    #filterset_fields = ["id"]  # In New version use filterset_fields
    #search_fields = ["name", "nick_name"]
    #ordering_fields = ["id"]


"""
class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)
"""


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


def auth(request):
    return render(request, "generator/oauth.html")