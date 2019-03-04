# Generated by Django 2.0.2 on 2018-10-30 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merchant_tools', '0040_auto_20181023_0648'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleButtonMaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_id', models.CharField(max_length=128, verbose_name='merchant id')),
                ('item_name', models.CharField(max_length=128)),
                ('item_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('item_number', models.CharField(max_length=128)),
                ('item_description', models.CharField(max_length=500)),
                ('invoice_number', models.CharField(max_length=128, null=True)),
                ('tax_amount', models.DecimalField(decimal_places=2, default=0, max_digits=20, null=True)),
                ('allow_shipping_cost', models.BooleanField(default=False)),
                ('shipping_cost', models.DecimalField(decimal_places=2, default=0, max_digits=20, null=True)),
                ('success_url_link', models.URLField(blank=True, max_length=128, null=True)),
                ('cancel_url_link', models.URLField(blank=True, max_length=128, null=True)),
                ('ipn_url_link', models.URLField(blank=True, max_length=128, null=True)),
                ('btn_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchant_tools.ButtonImage')),
            ],
        ),
    ]