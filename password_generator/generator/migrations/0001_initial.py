# Generated by Django 4.2.1 on 2023-06-08 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListPasswords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=255)),
                ('nick_name', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
