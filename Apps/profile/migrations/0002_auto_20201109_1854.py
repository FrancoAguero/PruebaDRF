# Generated by Django 2.2 on 2020-11-09 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cart',
            field=models.CharField(default="{'cart': []}", max_length=255),
        ),
    ]