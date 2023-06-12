from django.contrib.auth.models import User
from django.db import models
from rest_framework import generics


class PasswordsUserList(models.Model):
    password = models.CharField(max_length=30)
    resource = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    # owner = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        """For picture in admin panel"""
        return f'Id {self.id}: name {self.name}'



# test_one = ListPasswords.objects.create(password="test_password_1", name="test_1", nick_name="tester1")
# test_two = ListPasswords.objects.create(password="test_password_2", name="tester_2", nick_name="tester2")
