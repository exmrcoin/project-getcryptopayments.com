# Generated by Django 2.0.2 on 2018-09-28 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0030_auto_20180927_0702'),
        ('merchant_tools', '0023_auto_20180927_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='cryptopaymentrec',
            name='selected_erc_token',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coins.EthereumToken'),
        ),
        migrations.AlterField(
            model_name='cryptopaymentrec',
            name='selected_coin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coins.Coin'),
        ),
    ]