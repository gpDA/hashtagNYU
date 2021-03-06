# Generated by Django 2.1.1 on 2018-09-26 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_tweet'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='hour',
            field=models.IntegerField(default=11),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='day',
            field=models.IntegerField(default=59),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='favorite',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='min',
            field=models.IntegerField(default=59),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='retweet',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='year',
            field=models.IntegerField(default=2018),
        ),
    ]
