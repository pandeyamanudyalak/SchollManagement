# Generated by Django 4.2.6 on 2023-10-16 19:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('college_id', models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(limit_value=100000, message='College ID must be at least 6 digits.'), django.core.validators.MaxValueValidator(limit_value=999999, message='College ID must be at most 6 digits.')])),
                ('user_id', models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(limit_value=100000, message='User ID must be at least 6 digits.'), django.core.validators.MaxValueValidator(limit_value=999999, message='College ID must be at most 6 digits.')])),
                ('financial_year', models.CharField(choices=[('23-24', '2023-2024')], max_length=5)),
                ('is_active', models.BooleanField(choices=[('23-24', '2023-2024')], default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
