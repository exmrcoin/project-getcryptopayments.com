# Generated by Django 2.0.2 on 2018-04-05 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20180404_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='storecategory',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='storecategory',
            name='image',
            field=models.FileField(help_text='Add svg image of size 2137x2138 ', upload_to='store/category', verbose_name='image'),
        ),
    ]
