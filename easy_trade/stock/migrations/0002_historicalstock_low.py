# Generated by Django 3.2.15 on 2023-09-13 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalstock',
            name='low',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
