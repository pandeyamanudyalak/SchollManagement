# Generated by Django 4.2.6 on 2023-10-16 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='colleneg_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]