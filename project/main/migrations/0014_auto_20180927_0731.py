# Generated by Django 2.1.1 on 2018-09-27 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20180927_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='bg',
            field=models.URLField(default='https://images.pexels.com/photos/956981/milky-way-starry-sky-night-sky-star-956981.jpeg?auto=compress&cs=tinysrgb&h=350', max_length=500),
        ),
    ]
