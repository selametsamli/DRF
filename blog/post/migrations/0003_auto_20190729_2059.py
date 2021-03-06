# Generated by Django 2.2.3 on 2019-07-29 20:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20190729_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='craeted',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 29, 20, 59, 34, 451093, tzinfo=utc), editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=datetime.datetime(2019, 7, 29, 20, 59, 42, 869343, tzinfo=utc), upload_to='media/post/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 29, 20, 59, 49, 596216, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2019, 7, 29, 20, 59, 54, 871774, tzinfo=utc), editable=False, max_length=150, unique=True),
            preserve_default=False,
        ),
    ]
