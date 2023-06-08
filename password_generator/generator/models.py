from django.db import models


class ListPasswords(models.Model):
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=255)
    nick_name = models.CharField(max_length=255, default='')


    def __str__(self):
        """For picture in admin panel"""
        return f'Id {self.id}: name {self.name}'


#test_one = ListPasswords.objects.create(password="test_password_1", name="test_1", nick_name="tester1")
#test_two = ListPasswords.objects.create(password="test_password_2", name="tester_2", nick_name="tester2")