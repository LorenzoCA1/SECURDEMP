# Generated by Django 3.0.4 on 2020-03-26 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200326_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='SecurityQuestion',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
