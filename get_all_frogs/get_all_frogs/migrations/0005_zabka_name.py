# Generated by Django 5.0.3 on 2024-04-16 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_all_frogs', '0004_remove_visitedzabkas_zabka_visitedzabkas_zabka'),
    ]

    operations = [
        migrations.AddField(
            model_name='zabka',
            name='name',
            field=models.CharField(max_length=10, null=True),
        ),
    ]