# Generated by Django 2.0.2 on 2018-09-19 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coins', '0024_merge_20180913_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaypalTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=200)),
                ('coin_amount', models.CharField(max_length=200)),
                ('paypal_txid', models.CharField(max_length=200)),
                ('tx_status', models.BooleanField(default=False)),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coins.NewCoin', verbose_name='coin')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]