# Generated by Django 3.0.4 on 2020-04-08 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='call',
            field=models.CharField(help_text='Enter a 3 digit call number', max_length=3, null=True, verbose_name='Call Number'),
        ),
    ]