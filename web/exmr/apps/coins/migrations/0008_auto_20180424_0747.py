# Generated by Django 2.0.2 on 2018-04-24 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coins', '0007_merge_20180419_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private', models.CharField(blank=True, default='', max_length=500)),
                ('public', models.CharField(blank=True, default='', max_length=500)),
                ('words', models.CharField(blank=True, default='', max_length=500)),
                ('paymentid', models.CharField(blank=True, default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='WalletAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, default='', max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='wallet',
            name='addresses',
            field=models.ManyToManyField(to='coins.WalletAddress'),
        ),
        migrations.AddField(
            model_name='wallet',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coins.Coin'),
        ),
        migrations.AddField(
            model_name='wallet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]