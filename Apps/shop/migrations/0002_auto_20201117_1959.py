# Generated by Django 2.2 on 2020-11-17 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='added',
            new_name='created',
        ),
    ]
