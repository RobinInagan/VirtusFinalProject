# Generated by Django 5.0.3 on 2024-05-26 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_waiter_shift_restaurant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='FirstName',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='SecondName',
            new_name='lastName',
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]