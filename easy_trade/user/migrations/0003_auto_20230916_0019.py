# Generated by Django 3.2.15 on 2023-09-16 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userdocument_userotp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email address of User'),
        ),
    ]
