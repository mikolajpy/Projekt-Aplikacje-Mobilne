# Generated by Django 5.0.3 on 2024-04-16 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_all_frogs', '0005_zabka_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitedzabkas',
            name='zabka',
        ),
        migrations.AddField(
            model_name='visitedzabkas',
            name='zabka',
            field=models.ManyToManyField(to='get_all_frogs.zabka'),
        ),
    ]
