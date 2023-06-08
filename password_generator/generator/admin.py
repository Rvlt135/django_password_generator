from django.contrib import admin
from django.contrib.admin import ModelAdmin

from generator.models import ListPasswords


@admin.register(ListPasswords)
class ListPasswordsAdmin(ModelAdmin):
    """Class model for admin panel"""
    pass

