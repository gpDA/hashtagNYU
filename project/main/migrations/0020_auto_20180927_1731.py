# Generated by Django 2.1.1 on 2018-09-27 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20180927_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='background',
            field=models.URLField(default='https://www.cbronline.com/wp-content/uploads/2016/06/twitter2.png', max_length=500, null=True),
        ),
    ]
