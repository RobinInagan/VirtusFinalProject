# Generated by Django 5.0.3 on 2024-05-22 02:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Restaurant', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tables_restaurant',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Restaurant.restaurant'),
        ),
        migrations.AddField(
            model_name='tables_restaurant',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Restaurant.table'),
        ),
    ]
