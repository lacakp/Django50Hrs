# Generated by Django 3.2 on 2021-06-20 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_cart_stamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cartquan',
            field=models.IntegerField(default=0),
        ),
    ]
