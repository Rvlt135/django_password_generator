"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from rest_framework_swagger.views import get_swagger_view

from generator.views import home, generate_password, ViewPasswordList

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
# router.register(r'list_password', ViewPasswordList)
# schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
    # path(r'swagger/', schema_view),
    path('admin/', admin.site.urls),
    path('', home),
    path('password/', generate_password, name='password'),
    path('password_list/', ViewPasswordList.as_view()),
    path('password_list/<int:pk>/', ViewPasswordList.as_view()),

]

urlpatterns += router.urls