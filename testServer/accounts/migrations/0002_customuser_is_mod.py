# Generated by Django 4.0.4 on 2022-04-27 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_mod',
            field=models.BooleanField(default=False),
        ),
    ]