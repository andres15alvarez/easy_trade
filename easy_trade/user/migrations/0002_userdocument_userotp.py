# Generated by Django 3.2.15 on 2023-09-09 20:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOTP',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Register created timestamp')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Last update timestampt')),
                ('deleted_at', models.DateTimeField(blank=True, help_text='Soft deleted timestamp', null=True)),
                ('is_active', models.BooleanField(default=True, help_text='Indicate if the register is active')),
                ('otp', models.CharField(max_length=8)),
                ('method', models.CharField(max_length=50)),
                ('valid_at', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='otps', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_otp',
            },
        ),
        migrations.CreateModel(
            name='UserDocument',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Register created timestamp')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Last update timestampt')),
                ('deleted_at', models.DateTimeField(blank=True, help_text='Soft deleted timestamp', null=True)),
                ('is_active', models.BooleanField(default=True, help_text='Indicate if the register is active')),
                ('document', models.CharField(max_length=150)),
                ('document_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='catalog.document')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_document',
            },
        ),
    ]
