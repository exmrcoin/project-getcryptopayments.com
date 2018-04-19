# Generated by Django 2.0.2 on 2018-04-13 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='active',
            field=models.BooleanField(default=True, help_text='Disable this coin anytime'),
        ),
        migrations.AddField(
            model_name='coin',
            name='can_convert',
            field=models.BooleanField(default=True, verbose_name='can convert coin to another'),
        ),
        migrations.AddField(
            model_name='coin',
            name='can_donate',
            field=models.BooleanField(default=False, verbose_name='can donate coins'),
        ),
        migrations.AddField(
            model_name='coin',
            name='can_explore',
            field=models.BooleanField(default=False, verbose_name='can explore coins'),
        ),
        migrations.AddField(
            model_name='coin',
            name='fee_percentage',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='fee percentage'),
        ),
        migrations.AlterField(
            model_name='coin',
            name='image',
            field=models.ImageField(help_text='Upload a 35X35 image for better experience', upload_to='', verbose_name='image'),
        ),
    ]
