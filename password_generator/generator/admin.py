from django.contrib import admin
from django.contrib.admin import ModelAdmin

from generator.models import PasswordsUserList


@admin.register(PasswordsUserList)
class ListPasswordsAdmin(ModelAdmin):
    """Class model for admin panel"""
    pass

