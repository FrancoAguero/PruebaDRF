# Generated by Django 2.2 on 2020-11-17 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0003_auto_20201117_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cart',
            field=models.CharField(default='{"cart": []}', max_length=255),
        ),
    ]
