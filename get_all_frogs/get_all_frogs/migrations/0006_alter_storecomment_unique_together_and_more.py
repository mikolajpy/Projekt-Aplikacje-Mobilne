# Generated by Django 5.0.3 on 2024-05-11 10:00

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_all_frogs', '0005_alter_storecomment_ocena_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='storecomment',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='storecomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='get_all_frogs.storecomment'),
        ),
        migrations.AlterField(
            model_name='storecomment',
            name='Ocena',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddConstraint(
            model_name='storecomment',
            constraint=models.UniqueConstraint(condition=models.Q(('parent__isnull', True)), fields=('store', 'user'), name='unique_main_comment'),
        ),
    ]