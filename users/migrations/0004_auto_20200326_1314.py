# Generated by Django 3.0.4 on 2020-03-26 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200326_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='SecurityAnswer',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='SecurityQuestion',
        ),
    ]
