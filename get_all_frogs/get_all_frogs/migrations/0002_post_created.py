# Generated by Django 5.0.3 on 2024-04-23 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_all_frogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
