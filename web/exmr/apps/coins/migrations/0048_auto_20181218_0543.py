# Generated by Django 2.0.2 on 2018-12-18 05:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0047_auto_20181217_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paybyname',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 18, 5, 43, 15, 96833, tzinfo=utc)),
        ),
    ]